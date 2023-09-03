from reactpy.core.component import Component
from reactpy import component, html


@component
def sample_response(dark_theme) -> Component:
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
                    'Sample Response',
                    html.hr(),
                ),
                html.div(
                    {
                        'class_name': 'deskripsi-konten'
                    },
                    html.ul(
                        {
                            'class_name': 'nav nav-tabs',
                            'id': 'myTab',
                            'role': 'tablist'
                        },
                        html.li(
                            {
                                'class_name': 'nav-item',
                                'role': 'presentation'
                            },
                            html.button(
                                {
                                    'class_name': f'nav-link active {"text-dark" if dark_theme == False else "text-light"}',
                                    'id': 'rps/rps-random-success-tab',
                                    'data-bs-toggle': 'tab',
                                    'data-bs-target': '#rps/rps-random-success-tab-pane',
                                    'type': 'button',
                                    'role': 'tab',
                                    'aria-controls': 'rps/rps-random-success-tab-pane',
                                    'aria-selected': 'true'
                                },
                                'Response Success'
                            )
                        ),
                        html.li(
                            {
                                'class_name': 'nav-item',
                                'role': 'presentation'
                            },
                            html.button(
                                {
                                    'class_name': f'nav-link {"text-dark" if dark_theme == False else "text-light"}',
                                    'id': 'rps/rps-random-failed-tab',
                                    'data-bs-toggle': 'tab',
                                    'data-bs-target': '#rps/rps-random-failed-tab-pane',
                                    'type': 'button',
                                    'role': 'tab',
                                    'aria-controls': 'rps/rps-random-failed-tab-pane',
                                    'aria-selected': 'true'
                                },
                                'Response Failed'
                            )
                        ),
                    ),
                    html.div(
                        {
                            'class_name': 'tab-content',
                            'id': 'myTabContent'
                        },
                        html.div(
                            {
                                'class_name': 'tab-pane fade show active',
                                'id': 'rps/rps-random-success-tab-pane',
                                'role': 'tabpanel',
                                'aria-labelledby': 'rps/rps-random-success-tab',
                                'tabindex': '0'
                            },
                            html.pre(
                                {
                                    'class_name': 'text-light bg-dark'
                                },
                                html.code(
                                    '''[
    {
        'ditttt-rps': {
            'result': [
                'scissors',
                'rock',
                'scissors',
                'paper',
                'paper'
            ],
            'status_code': 200
        }
    }
]'''
                                )
                            )
                        ),
                        html.div(
                            {
                                'class_name': 'tab-pane fade',
                                'id': 'rps/rps-random-failed-tab-pane',
                                'role': 'tabpanel',
                                'aria-labelledby': 'rps/rps-random-failed-tab',
                                'tabindex': '0'
                            },
                            html.pre(
                                {
                                    'class_name': 'text-light bg-dark'
                                },
                                html.code(
                                    '''[
    {
        'ditttt-rps': {
            'result': 'The number must must be 1 - 5',
            'status_code': 400
        }
    }
]'''
                                )
                            )
                        ),
                    )
                ),
                html.hr()
            )
        ),
    )
