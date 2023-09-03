from reactpy.core.component import Component
from reactpy import component, html


@component
def sample_request() -> Component:
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
                    'Sample Request URL',
                    html.hr(),
                ),
                html.div(
                    {
                        'class_name': 'deskripsi-konten'
                    },
                    html.a(
                        {
                            'href': 'http://127.0.0.1:8000/rps/vs-bot/rock',
                            'target': '_blank'
                        },
                        'http://127.0.0.1:8000/rps/vs-bot/rock'
                    )
                ),
                html.hr()
            )
        ),
    )
