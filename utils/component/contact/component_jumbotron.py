from reactpy.core.component import Component
from reactpy import component, html, use_state
from .contact_form import contact_form


@component
def component_jumbotron(is_dark_theme) -> Component:
    return html._(
        html.section(
            {
                'class_name': 'jumbotron pb-3',
                'id': 'jumbotron',
                'style':
                    {
                        'background-color': '#0F172A' if is_dark_theme else '',
                        'padding-top': '90px'
                    }
            },
            html.div(
                {
                    'class_name': 'container'
                },
                html.section(
                    {
                        'class_name': 'border border-black rounded form',
                        'id': 'border form',
                        'style': {
                            'margin-left': '17.5%',
                            'margin-right': '17.5%'
                        }
                    },
                    html.div(
                        {
                            'class_name': 'row me-3 ms-3 mt-3'
                        },
                        html.div(
                            {
                                'class_name': 'col'
                            },
                            html.p(
                                {
                                    'class_name': f'judul judul-1 text-center {"text-light" if is_dark_theme else "text-dark"}',
                                },
                                'Contact Form',
                            ),
                        ),
                    ),
                    html.div(
                        {
                            'class_name': 'row me-3 ms-3'
                        },
                        html.div(
                            {
                                'class_name': 'col'
                            },
                            contact_form(is_dark_theme)
                        )
                    )
                ),
            ),
        ),
    )
