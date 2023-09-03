from reactpy.core.component import Component
from reactpy import component, html
from reactpy.core.vdom import make_vdom_constructor
from .component_card import component_card


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
                        'class_name': 'border border-black rounded border-konten-donate',
                        'id': 'border',
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
                                'Donation',
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
                            html.p(
                                {
                                    'class_name': f'text-center {"text-light" if is_dark_theme else "text-dark"}',
                                    'style': {
                                        'font-size': '13px'
                                    }
                                },
                                'Your help is the motivation that really helps us to do extraordinary things and continue to work.',
                            ),
                        ),
                    ),
                    html.div(
                        {
                            'class_name': 'row me-3 ms-3 mt-4'
                        },
                        html.div(
                            {
                                'class_name': 'col'
                            },
                            component_card()
                        ),
                    ),
                ),
            ),
        ),
    )
