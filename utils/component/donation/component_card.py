from reactpy.core.component import Component
from reactpy import component, html
from reactpy.core.vdom import make_vdom_constructor


@component
def component_card() -> Component:
    return html._(
        html.div(
            {
                'class_name': 'card'
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
                            'src': '../../../static/image/saweria.ico',
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
                    'Saweria'
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
        html.div(
            {
                'class_name': 'card mt-3'
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
                            'src': '../../../static/image/trakteer.png',
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
                    'Trakteer'
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
        html.div(
            {
                'class_name': 'card mt-3 mb-3'
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
                            'src': '../../../static/image/paypal.ico',
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
                    'Paypal'
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
        )
    )
