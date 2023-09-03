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
                        'choice'
                    ),
                    html.td(
                        'rock | paper | scissors'
                    ),
                    html.td(
                        'string'
                    ),
                    html.td(
                        'true'
                    ),
                    html.td(
                        'choose this parameter as you wish it should be rock paper or scissors'
                    )
                )
            )
        ),
        accordion_request(),
        html.hr(),
    )
