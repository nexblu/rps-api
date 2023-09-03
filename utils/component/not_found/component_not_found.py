from reactpy.core.component import Component
from reactpy import component, html
from reactpy.core.vdom import make_vdom_constructor


@component
def component_not_found(is_dark_theme) -> Component:
    return html._(
        html.section(
            {
                'id': '404-not-found',
                'class_name': f'{"bg-dark text-light" if is_dark_theme else "bg-light text-dark"}'
            },
            html.div(
                {
                    'class_name': 'container justify-content-center align-items-center d-flex text-center',
                    'style': {
                        'height': '100vh',
                        'width': '100%',
                    }
                },
                html.div(
                    {
                        'class_name': 'row'
                    },
                    html.div(
                        {
                            'class_name': 'col'
                        },
                        html.h2(
                            'Oops! Page Not Found.'
                        ),
                        html.h1(
                            {
                                'class_name': 'fw-bold',
                                'style': {
                                    'font-size': '150px'
                                },
                            },
                            '404',
                        ),
                        html.p(
                            'We Cant Find the page you\'re looking for.'.title()
                        ),
                        html.a(
                            {
                                'href': '/',
                                'class_name': 'text-light',
                                'style': {
                                        'text-decoration': 'none'
                                }
                            },
                            html.button(
                                {
                                    'class_name': 'btn btn-not-found text-light',
                                    'type': 'submit',
                                },
                                'Go Back Documentation'
                            ),
                        ),
                    )
                )
            )
        ),
    )
