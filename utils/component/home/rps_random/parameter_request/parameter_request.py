from reactpy.core.component import Component
from reactpy import component, html
from .table_request import table_request


@component
def parameter_request() -> Component:
    return html._(
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
                        'class_name': 'judul judul-2'
                    },
                    'Parameter Request',
                    html.hr(),
                ),
                table_request()
            )
        ),
    )
