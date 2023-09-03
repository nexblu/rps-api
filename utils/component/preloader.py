from reactpy.core.component import Component
from reactpy import component, html
from reactpy.core.vdom import make_vdom_constructor


@component
def preloader() -> Component:
    return html._(
        html.div(
            {
                'class_name': 'preloader bg-dark d-flex justify-content-center align-items-center',
                'style': {
                    'height': '100vh',
                }
            },
            html.div(
                {
                    'class_name': 'spinner-border text-info',
                    'role': 'status'
                },
                html.span(
                    {
                        'class_name': 'visually-hidden'
                    }
                )
            )
        )
    )
