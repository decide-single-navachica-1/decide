import json
from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404
from visualizer import metrics


from base import mods


class VisualizerView(TemplateView):
    template_name = 'visualizer/visualizer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)

        try:
            r = mods.get('voting', params={'id': vid})
            context['voting'] = json.dumps(r[0])
            context['abstentions'] = metrics.abstentions(vid)
        except:
            raise Http404

        return context

class VisualizerQuestion(TemplateView):
    template_name = 'visualizer/question/visualizer.html'
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('question_id', 0)
        
        try:
            res = []
            abs = []
            r = mods.get('voting', params={'question_id': vid})
            for ri in r :
                res.append(json.dumps(ri))
                abs.append(metrics.abstentions(json.dumps(ri).id))
            context['votings'] = res
            context['abstentions'] = abs
        except:
            raise Exception(res)

       	return context
        
class VisualizerAll(TemplateView):
    template_name = 'visualizer/all.html'
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            res = []
            r = mods.get('voting')
            for ri in r :
                res.append(json.dumps(ri))
            unstarted = metrics.unstartedVotings()
            started = metrics.startedVotings()
            finished = metrics.finishedVotings()
            closed = metrics.closedVotings()
            context['votings'] = res
            context['unstarted'] = unstarted
            context['started'] = started
            context['finished'] = finished
            context['closed'] = closed
        except:
            raise Http404

       	return context

