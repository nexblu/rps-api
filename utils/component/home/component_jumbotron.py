from reactpy.core.component import Component
from reactpy import component, html
from reactpy.core.vdom import make_vdom_constructor
from .rps_random import component_rps_random
from .rps_vs_bot import component_rps_vs_bot


@component
def component_jumbotron(is_dark_theme) -> Component:
    return html._(
        html.section(
            {
                'class_name': 'jumbotron pb-3',
                'id': 'jumbotron',
                'style': {
                    'min-height': '100vh',
                    'background-color': '#0F172A' if is_dark_theme else '',
                    'padding-top': '90px'
                },
            },
            html.div(
                {
                    'class_name': 'container'
                },
                html.section(
                    {
                        'class_name': f'border border-black rounded {"text-light" if is_dark_theme else "text-dark"}',
                        'id': 'border',
                        'style': {
                            'background-color': '#1E293B' if is_dark_theme else '#f0f0f0'
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
                                    'class_name': 'judul judul-1'
                                },
                                'Ditttt RPS API',
                                html.hr(),
                            ),
                            html.div(
                                {
                                    'class_name': 'deskripsi-konten'
                                },
                                'Ditttt RPS API was created to make it easier for developers to create rock paper scissors game applications'.title()
                            ),
                            html.hr()
                        )
                    ),
                    component_rps_random(is_dark_theme),
                    component_rps_vs_bot(is_dark_theme),
                )
            ),
        ),
    )
