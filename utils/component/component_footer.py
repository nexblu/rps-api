from reactpy.core.component import Component
from reactpy import component, html
from reactpy.core.vdom import make_vdom_constructor


@component
def component_footer() -> Component:
    ion_icon = make_vdom_constructor('ion-icon')

    footer_icon = {
        'instagram': {
            'href': 'https://www.instagram.com/ditttt.prm/',
            'target': '_blank',
            'name': 'logo-instagram'
        },
        'github': {
            'target': '_blank',
            'href': 'https://github.com/Ditttt?tab=repositories',
            'name': 'logo-github'
        },
        'contact': {
            'href': '/contact',
            'target': '',
            'name': 'mail-open-outline'
        },
        'store': {
            'target': '_blank',
            'href': 'https://itemku.com/t/boedoet-store?search_keyword=Boedoet%20Store&searchquery=Boedoet%20St&from=searchhomepage',
            'name': 'storefront-outline'
        },
        'donation': {
            'href': '/donation',
            'target': '',
            'name': 'cash-outline'
        }
    }

    component_icon = []
    for key, value in footer_icon.items():
        component_icon.append(
            html.a(
                {
                    'target': value['target'],
                    'href': value['href'],
                    'class_name': 'text-decoration-none text-dark'
                },
                ion_icon(
                    {
                        'name': value['name'],
                    }
                )
            ),
        )

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
                        component_icon
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
