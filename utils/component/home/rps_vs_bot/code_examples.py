from reactpy.core.component import Component
from reactpy import component, html


@component
def code_examples(dark_theme) -> Component:
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
                    'Code Examples',
                    html.hr(),
                ),
                html.nav(
                    {
                        'class_name': 'nav nav-tabs deskripsi-konten',
                        'id': 'nav-tab',
                        'role': 'tablist'
                    },
                    html.button(
                        {
                            'class_name': f'nav-link active {"text-dark" if dark_theme == False else "text-light"}',
                            'id': 'nav-rps-vs-bot-python-tab',
                            'data-bs-toggle': 'tab',
                            'data-bs-target': '#nav-rps-vs-bot-python',
                            'type': 'button',
                            'role': 'tab',
                            'aria-controls': 'nav-rps-vs-bot-python',
                            'aria-selected': 'true'
                        },
                        'Python'
                    ),
                    html.button(
                        {
                            'class_name': f'nav-link {"text-dark" if dark_theme == False else "text-light"}',
                            'id': 'nav-rps-vs-bot-javascript-tab',
                            'data-bs-toggle': 'tab',
                            'data-bs-target': '#nav-rps-vs-bot-javascript',
                            'type': 'button',
                            'role': 'tab',
                            'aria-controls': 'nav-rps-vs-bot-javascript',
                            'aria-selected': 'true'
                        },
                        'JavaScript'
                    ),
                    html.button(
                        {
                            'class_name': f'nav-link {"text-dark" if dark_theme == False else "text-light"}',
                            'id': 'nav-rps-vs-bot-lua-tab',
                            'data-bs-toggle': 'tab',
                            'data-bs-target': '#nav-rps-vs-bot-lua',
                            'type': 'button',
                            'role': 'tab',
                            'aria-controls': 'nav-rps-vs-bot-lua',
                            'aria-selected': 'true'
                        },
                        'Lua'
                    ),
                    html.button(
                        {
                            'class_name': f'nav-link {"text-dark" if dark_theme == False else "text-light"}',
                            'id': 'nav-rps-vs-bot-curl-tab',
                            'data-bs-toggle': 'tab',
                            'data-bs-target': '#nav-rps-vs-bot-curl',
                            'type': 'button',
                            'role': 'tab',
                            'aria-controls': 'nav-rps-vs-bot-curl',
                            'aria-selected': 'true'
                        },
                        'Curl'
                    )
                ),
                html.div(
                    {
                        'class_name': 'tab-content',
                        'id': 'nav-tabContent'
                    },
                    html.div(
                        {
                            'class_name': 'tab-pane fade show active',
                            'id': 'nav-rps-vs-bot-python',
                            'role': 'tabpanel',
                            'aria-labelledby': 'nav-rps-vs-bot-python-tab',
                            'tabindex': '0'
                        },
                        html.pre(
                            {
                                'class_name': 'bg-dark text-light'
                            },
                            html.code(
                                '''import requests
api_url = 'http://127.0.0.1:8000/rps/vs-bot/rock'
response = requests.get(api_url)
if response.status_code == 200:
    resp = response.json()
    print(resp)
else:
    resp = response.json()
    print(resp)'''
                            )
                        )
                    )
                ),
                html.div(
                    {
                        'class_name': 'tab-content',
                        'id': 'nav-tabContent'
                    },
                    html.div(
                        {
                            'class_name': 'tab-pane fade',
                            'id': 'nav-rps-vs-bot-javascript',
                            'role': 'tabpanel',
                            'aria-labelledby': 'nav-rps-vs-bot-javascript-tab',
                            'tabindex': '0'
                        },
                        html.pre(
                            {
                                'class_name': 'bg-dark text-light'
                            },
                            html.code(
                                '''const api_url = 'http://127.0.0.1:8000/rps/vs-bot/rock';
fetch(api_url)
    .then(response => {
        if (response.status === 200) {
        return response.json();
        } else {
        return response.json().then(data => {
            throw new Error(data.message);
        });
        }
    })
    .then(resp => {
        console.log(resp);
    })
    .catch(error => {
        console.error(error);
    })'''
                            )
                        )
                    )
                ),
                html.div(
                    {
                        'class_name': 'tab-content',
                        'id': 'nav-tabContent'
                    },
                    html.div(
                        {
                            'class_name': 'tab-pane fade',
                            'id': 'nav-rps-vs-bot-lua',
                            'role': 'tabpanel',
                            'aria-labelledby': 'nav-rps-vs-bot-lua-tab',
                            'tabindex': '0'
                        },
                        html.pre(
                            {
                                'class_name': 'bg-dark text-light'
                            },
                            html.code(
                                '''local http = require('socket.http')
local json = require('json')

local api_url = 'http://127.0.0.1:8000/rps/vs-bot/rock'
local response, status, headers = http.request(api_url)

if status == 200 then
    local resp = json.decode(response)
    for key, value in pairs(resp) do
        print(key, value)
    end
else
    local resp = json.decode(response)
    print('Error:', resp.message)
end'''
                            )
                        )
                    )
                ),
                html.div(
                    {
                        'class_name': 'tab-content',
                        'id': 'nav-tabContent'
                    },
                    html.div(
                        {
                            'class_name': 'tab-pane fade',
                            'id': 'nav-rps-vs-bot-curl',
                            'role': 'tabpanel',
                            'aria-labelledby': 'nav-rps-vs-bot-curl-tab',
                            'tabindex': '0'
                        },
                        html.pre(
                            {
                                'class_name': 'bg-dark text-light'
                            },
                            html.code(
                                '''curl http://127.0.0.1:8000/rps/vs-bot/rock'''
                            )
                        )
                    )
                ),
                html.hr(),
            ),
        ),
    )
