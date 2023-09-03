from reactpy.core.component import Component
from reactpy import component, html
from reactpy.core.vdom import make_vdom_constructor
from .accordion_request import accordion_request


@component
def table_request() -> Component:
    return html._(
        html.table(
            {
                'class_name': 'table table-dark text-center deskripsi-konten table-responsive'
            },
            html.thead(
                html.tr(
                    html.th(
                        {
                            'scope': 'col'
                        },
                        'Name'
                    ),
                    html.th(
                        {
                            'scope': 'col'
                        },
                        'Value'
                    ),
                    html.th(
                        {
                            'scope': 'col'
                        },
                        'Type'
                    ),
                    html.th(
                        {
                            'scope': 'col'
                        },
                        'Required'
                    ),
                    html.th(
                        {
                            'scope': 'col'
                        },
                        'Description'
                    )
                )
            ),
            html.tbody(
                html.tr(
                    html.td(
                        'amount'
                    ),
                    html.td(
                        '1 - 5'
                    ),
                    html.td(
                        'integer'
                    ),
                    html.td(
                        'true'
                    ),
                    html.td(
                        'to return rock paper or scissors randomly and the value must be 1 to 5 which is a number'
                    )
                )
            )
        ),
        accordion_request(),
        html.hr(),
    )
