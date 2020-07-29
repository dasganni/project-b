from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from guardian.mixins import PermissionListMixin, PermissionRequiredMixin
from guardian.shortcuts import assign_perm, remove_perm

from . import forms
from .models import Game


# Create your views here.
class createGame(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = "game/create_game.html"
    form_class = forms.createGameForm
    model = Game
    accept_global_perms = True
    permission_object = None
    permission_required = ["game.add_game"]
    return_403 = True

    def form_valid(self, form):
        form.instance.creator = self.request.user
        self.object = form.save(commit=True)
        assign_perm("view_game", self.request.user, self.object)
        assign_perm("change_game", self.request.user, self.object)
        assign_perm("delete_game", self.request.user, self.object)
        if self.object.access_restricted:
            for allowed_player in form.cleaned_data.get('allowed_players'):
                assign_perm("view_game", allowed_player, self.object)
        else:
            default_usergroup = Group.objects.get(name="default_usergroup")
            assign_perm("view_game", default_usergroup, self.object)
        return super(createGame, self).form_valid(form)


class updateGame(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = "game/update_game.html"
    form_class = forms.updateGameForm
    model = Game
    pk_url_kwarg = "game_id"
    # Django Guardian Rights
    accept_global_perms = True
    permission_required = "game.change_game"
    return_403 = True

    def form_valid(self, form):
        prechange_object = self.get_object()
        prechange_access_restricted = prechange_object.access_restricted
        #get changed rights
        set_prechange = set((x.username) for x in prechange_object.allowed_players.all())
        set_postchange = set((x.username) for x in form.cleaned_data.get('allowed_players'))
        rights_to_add = [x for x in form.cleaned_data.get('allowed_players') if x.username not in set_prechange]
        rights_to_remove = [x for x in prechange_object.allowed_players.all() if x.username not in set_postchange]

        self.object = form.save(commit=True)
        
        #remove default_roup access
        if self.object.access_restricted:
            if not prechange_access_restricted:
                default_usergroup = Group.objects.get(name="default_usergroup")
                remove_perm("view_game", default_usergroup, self.object)
        #assign default_group access
        else:
            if prechange_access_restricted:
                default_usergroup = Group.objects.get(name="default_usergroup")
                assign_perm("view_game", default_usergroup, self.object)

        #add or remove user rights
        for x in rights_to_add:
            assign_perm("view_game", x, self.object)
        for x in rights_to_remove:
            remove_perm("view_game", x, self.object)
        return super(updateGame, self).form_valid(form)


class deleteGame(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Game
    pk_url_kwarg = "game_id"
    # Django Guardian Rights
    accept_global_perms = True
    permission_required = "game.delete_game"
    return_403 = True


class listGames(LoginRequiredMixin, PermissionListMixin, ListView):
    template_name = "game/games_list.html"
    model = Game
    permission_required = "game.view_game"
    get_objects_for_user_extra_kwargs = {"use_groups": True}
