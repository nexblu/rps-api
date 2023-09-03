from reactpy.core.component import Component
from reactpy import component, html
from reactpy.core.vdom import make_vdom_constructor


@component
def jump_top(url) -> Component:
    ion_icon = make_vdom_constructor('ion-icon')
    return html._(
        html.div(
            {
                'class_name': 'jump-top d-flex justify-content-center'
            },
            html.a(
                {
                    'href': url,
                    'class_name': 'position-fixed fixed-bottom-left text-decoration-none text-light p-4',
                    'style': {
                        'z-index': '9999',
                        'bottom': '4px',
                        'right': '4px',
                    }
                },
                ion_icon(
                    {
                        'name': 'arrow-up-circle-outline',
                    }
                )
            ),
        ),
    )
