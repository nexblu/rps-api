from fastapi import FastAPI
from reactpy import component, html, web, use_state, use_location
from reactpy.backend.fastapi import configure, Options
from reactpy_router import route, simple
from reactpy.core.component import Component
from utils import component_home, RpsAPI, component_contact, component_donation, component_404
from fastapi.responses import JSONResponse
from reactpy import web, use_state, use_effect
from asyncio import sleep
from reactpy.core.vdom import make_vdom_constructor
from reactpy.backend.types import Location
import json
from pathlib import Path
from fastapi.staticfiles import StaticFiles


@component
def coba() -> Component:
    return html._(
        html.style(
            '''
            :root {
                --color-light: #F8F6EE;
                --color-dark: #212529;
            }
            
            .accordion{
                --bs-accordion-bg: var(--color-dark);
                --bs-accordion-color: var(--color-light);
                --bs-accordion-btn-color: var(--color-light);
                --bs-accordion-btn-bg: #08956E;
                --bs-accordion-btn-focus-box-shadow: none;
                --bs-accordion-active-bg: #1fa37d;
                --bs-accordion-active-color: var(--color-light);
            }
            '''
        ),
        html.div(
            {
                'class_name': 'accordion',
                'id': 'accordionExample'
            },
            html.div(
                {
                    'class_name': 'accordion-item'
                },
                html.h2(
                    {
                        'class_name': 'accordion-header'
                    },
                    html.button(
                        {
                            'class_name': 'accordion-button',
                            'type': "button",
                            'data-bs-toggle': "collapse",
                            'data-bs-target': "#collapseOne",
                            'aria-expanded': "true",
                            'aria-controls': "collapseOne"
                        },
                        'amount', html.span(
                            {
                                'style': {
                                    'color': '#dddcd4'
                                },
                                'class_name': 'ms-1'
                            },
                            'required | integer'
                        )
                    )
                ),
                html.div(
                    {
                        'id': "collapseOne",
                        'class_name': "accordion-collapse collapse show",
                        'data-bs-parent': "#accordionExample"
                    },
                    html.div(
                        {
                            'class_name': 'accordion-body'
                        },
                        'to return rock paper or scissors randomly and the value must be 1 to 5 which is a number'
                    )
                )
            )
        )
    )


@component
def root() -> Component:
    return simple.router(
        route('/', component_home()),
        route('/contact', component_contact()),
        route('/donation', component_donation()),
        route('/coba', coba()),
        route('*', component_404()),
    )


app = FastAPI()
api = RpsAPI()

static_folder = 'static'
app.mount('/static', StaticFiles(directory=static_folder), name='static')


@app.get('/rps/random/{amount}')
def rps_random(amount: str) -> JSONResponse:
    return api.get_random(amount)


@app.get('/rps/vs-bot/{choice}')
def rps_random(choice: str) -> JSONResponse:
    return api.vs_bot(choice)


configure(app, root, options=Options(
    head=html._(
        html.meta(
            {"name": "viewport", "content": "width=device-width, initial-scale=1"}
        ),
        html.link(
            {
                'href': 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css',
                'rel': 'stylesheet',
                'integrity': 'sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9',
                'crossorigin': 'anonymous'
            }
        ),
        html.script(
            {
                'src': 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js',
                'integrity': 'sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm',
                'crossorigin': 'anonymous'
            }
        ),
        html.link(
            {
                'rel': 'stylesheet',
                'href': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css'
            }
        ),
        html.script(
            {
                'src': 'https://kit.fontawesome.com/cdf7b08825.js',
                'crossorigin': 'anonymous'
            }
        ),
        html.script(
            {
                'type': 'module',
                'src': 'https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js'
            }
        ),
        html.script(
            {
                'nomodule': True,
                'src': 'https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js'
            }
        ),
    )
))
