# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2010-2011, GEM Foundation.
#
# OpenQuake is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# only, as published by the Free Software Foundation.
#
# OpenQuake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License version 3 for more details
# (a copy is included in the LICENSE file that accompanied this code).
#
# You should have received a copy of the GNU Lesser General Public License
# version 3 along with OpenQuake.  If not, see
# <http://www.gnu.org/licenses/lgpl-3.0.txt> for a copy of the LGPLv3 License

from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect

from geonode.observations import models
from geonode.observations import forms


def edit(request, observation_id, summary_id):
    """
    The view that returns the Id filed from the fault summary table.
    """

    if request.method == 'POST':
        if observation_id and summary_id:
            o = get_object_or_404(models.Observation, pk=observation_id)
            o.summary_id = summary_id
            form = forms.Observation(request.POST, instance=o)
        else:
            form = forms.Observation(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response("obsform_form.html",
                      {'form': form,
                       'success' : 'Your observation was saved'},
                context_instance=RequestContext(request))
    else:
        o = get_object_or_404(models.Observation, pk=observation_id)
        o.summary_id = summary_id

        form = forms.Observation(instance=o)

    return render_to_response('obsform_form.html', {'form' : form},
                              context_instance=RequestContext(request))
