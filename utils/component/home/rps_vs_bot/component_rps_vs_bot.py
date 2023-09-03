from reactpy.core.component import Component
from reactpy import component, html
from .code_examples import code_examples
from .parameter_request.parameter_request import parameter_request
from .sample_request import sample_request
from .sample_response import sample_response


@component
def component_rps_vs_bot(dark_theme) -> Component:
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
                    'rps/vs-bot (GET)',
                    html.hr(),
                ),
                html.div(
                    {
                        'class_name': 'deskripsi-konten'
                    },
                    'to play with bot'.title(
                    )
                ),
                html.hr()
            )
        ),
        sample_request(),
        parameter_request(),
        code_examples(dark_theme),
        sample_response(dark_theme)
    )
