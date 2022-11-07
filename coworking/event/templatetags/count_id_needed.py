from django import template

register = template.Library()


@register.simple_tag()
def count_id_needed(slide_num, on_slide_num, events_per_slide):
    return slide_num * events_per_slide + on_slide_num
