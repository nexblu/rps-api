from reactpy.core.component import Component
from reactpy import component, html
from reactpy.core.vdom import make_vdom_constructor


@component
def component_card() -> Component:
    content_card = {
        'saweria': {
            'icon_url': '../../../static/image/saweria.ico'
        },
        'Trakteer': {
            'icon_url': '../../../static/image/trakteer.png'
        },
        'Paypal': {
            'icon_url': '../../../static/image/paypal.ico'
        }
    }

    card = []
    index = 0
    for key, value in content_card.items():
        card.append(
            html.div(
                {
                    'class_name': f'card {"mt-3" if index > 0 else ""} {"mb-3" if len(content_card) == index + 1 else ""}'
                },
                html.div(
                    {
                        'class_name': 'card-body d-flex'
                    },
                    html.div(
                        {
                            'class_name': 'border rounded'
                        },
                        html.img(
                            {
                                'src': value['icon_url'],
                                'class_name': 'm-2',
                                'style': {
                                    'width': '30px',
                                    'height': '30px'
                                }
                            }
                        )
                    ),
                    html.span(
                        {
                            'class_name': 'ms-3',
                            'style': {
                                'margin-top': '12px'
                            }
                        },
                        key
                    ),
                    html.button(
                        {
                            'class_name': 'btn btn-donate btn-donate-extra-small ms-auto text-light'
                        },
                        'Donate'
                    )
                ),
                html.button(
                    {
                        'class_name': 'btn btn-donate btn-donate-extra-small-active m-2 me-auto text-light'
                    },
                    'Donate'
                )
            ),
        )
        index += 1

    return html._(
        card
    )
