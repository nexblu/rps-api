from reactpy.core.component import Component
from reactpy import component, html
from reactpy.core.vdom import make_vdom_constructor


@component
def accordion_request() -> Component:
    return html._(
        html.div(
            {
                'class_name': 'accordion',
                'id': 'accordion-rps-random'
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
                        'amount', html.span(
                            {
                                'style': {
                                    'color': '#dddcd4'
                                },
                                'class_name': 'ms-1'
                            },
                            'required | integer'
                        )
                    )
                ),
                html.div(
                    {
                        'id': "collapseOne",
                        'class_name': "accordion-collapse collapse show",
                        'data-bs-parent': "#accordion-rps-random"
                    },
                    html.div(
                        {
                            'class_name': 'accordion-body'
                        },
                        'to return rock paper or scissors randomly and the value must be 1 to 5 which is a number'
                    )
                )
            )
        ),
    )
