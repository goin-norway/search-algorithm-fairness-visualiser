from django_components import component


@component.register("button")
class Button(component.Component):
    template_name = "button/button.html"

    def get_context_data(self, text, link, empty_style_button=False):
        return {
            "text": text,
            "link": link,
            "button_class": "empty" if empty_style_button else "coloured",
        }
        
    class Media:
        css = "button/button.css"
