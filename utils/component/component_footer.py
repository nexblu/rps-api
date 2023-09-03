from reactpy.core.component import Component
from reactpy import component, html
from reactpy.core.vdom import make_vdom_constructor


@component
def component_footer() -> Component:
    ion_icon = make_vdom_constructor('ion-icon')
    return html._(
        html.footer(
            {
                'class_name': 'p-3',
                'style': {
                    'background-color': '#2B2F3E'
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
                    html.p(
                        {
                            'class_name': 'text-center text-light fw-bold'
                        },
                        'Connect With Us'
                    )
                ),
            ),
            html.div(
                {
                    'class_name': 'row'
                },
                html.div(
                    {
                        'class_name': 'col'
                    },
                    html.div(
                        {
                            'class_name': 'social-icon d-flex justify-content-center'
                        },
                        html.a(
                            {
                                'target': '_blank',
                                'href': 'https://www.instagram.com/ditttt.prm/',
                                'class_name': 'text-decoration-none text-dark'
                            },
                            ion_icon(
                                {
                                    'name': 'logo-instagram',
                                }
                            )
                        ),
                        html.a(
                            {
                                'target': '_blank',
                                'href': 'https://github.com/Ditttt?tab=repositories',
                                'class_name': 'text-decoration-none text-dark'
                            },
                            ion_icon(
                                {
                                    'name': 'logo-github',
                                }
                            )
                        ),
                        html.a(
                            {
                                'href': '/contact',
                                'class_name': 'text-decoration-none text-dark'
                            },
                            ion_icon(
                                {
                                    'name': 'mail-open-outline',
                                }
                            )
                        ),
                        html.a(
                            {
                                'target': '_blank',
                                'href': 'https://itemku.com/t/boedoet-store?search_keyword=Boedoet%20Store&searchquery=Boedoet%20St&from=searchhomepage',
                                'class_name': 'text-decoration-none text-dark'
                            },
                            ion_icon(
                                {
                                    'name': 'storefront-outline',
                                }
                            )
                        ),
                        html.a(
                            {
                                'href': '/donation',
                                'class_name': 'text-decoration-none text-dark'
                            },
                            ion_icon(
                                {
                                    'name': 'cash-outline',
                                }
                            )
                        )
                    ),
                    html.hr(
                        {
                            'class_name': 'text-light'
                        }
                    )
                ),
            ),
            html.div(
                {
                    'class_name': 'row'
                },
                html.div(
                    {
                        'class_name': 'col'
                    },
                    html.p(
                        {
                            'class_name': 'text-center text-light pt-3 fw-bold'
                        },
                        '© 2023. Created By Andana Farras Pramudita'
                    )
                )
            )
        )
    )
