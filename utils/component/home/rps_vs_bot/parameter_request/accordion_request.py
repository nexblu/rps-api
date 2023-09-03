from reactpy.core.component import Component
from reactpy import component, html
from reactpy.core.vdom import make_vdom_constructor


@component
def accordion_request() -> Component:
    return html._(
        html.div(
            {
                'class_name': 'accordion',
                'id': 'accordion-rps-vs-bot accordion-parameter-request'
            },
            html.div(
                {
                    'class_name': 'accordion-item'
                },
                html.h2(
                    {
                        'class_name': 'accordion-header'
                    },
                    html.button(
                        {
                            'class_name': 'accordion-button',
                            'type': "button",
                            'data-bs-toggle': "collapse",
                            'data-bs-target': "#collapseOne",
                            'aria-expanded': "true",
                            'aria-controls': "collapseOne"
                        },
                        'choice',
                        html.span(
                            {
                                'style': {
                                    'color': '#dddcd4'
                                },
                                'class_name': 'ms-1'
                            },
                            'required | string'
                        )
                    )
                ),
                html.div(
                    {
                        'id': "collapseOne",
                        'class_name': "accordion-collapse collapse show",
                        'data-bs-parent': "#accordion-rps-vs-bot"
                    },
                    html.div(
                        {
                            'class_name': 'accordion-body'
                        },
                        'choose this parameter as you wish it should be rock paper or scissors'
                    )
                )
            )
        ),
    )
