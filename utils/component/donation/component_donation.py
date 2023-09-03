from reactpy.core.component import Component
from reactpy import component, html, use_effect, use_location, use_state, web
from reactpy.core.vdom import make_vdom_constructor
from reactpy.backend.types import Location
from asyncio import sleep
from .component_jumbotron import component_jumbotron
from ..component_footer import component_footer
from ..jump_top import jump_top
from ..preloader import preloader as preload


@component
def component_donation() -> Component:
    location: Location = use_location()
    selected_option_theme, set_selected_option_theme = use_state(None)
    is_dark_theme, set_is_dark_theme = use_state(True)
    is_open_theme, set_is_open_theme = use_state(False)

    is_loading, set_loading = use_state(True)

    def toggle_dropdown_theme(event):
        set_is_open_theme(not is_open_theme)

    def handle_option_click_theme(value, theme):
        set_selected_option_theme(value)
        set_is_dark_theme(theme)
        set_is_open_theme(False)

    @use_effect
    async def loading():
        await sleep(5)
        set_loading(False)

    return html._(
        html.script(
            {
                'type': 'text/javascript'
            },
            '''
var link = document.querySelector("link[rel~='icon']");
if (!link) {
    link = document.createElement('link');
    link.rel = 'icon';
    document.head.appendChild(link);
}
link.href = '../../../static/image/rps-api-icon.png';
document.title = 'Donation Ditttt RPS API';
'''
        ),
        (
            html.style(
                '''
            @import url('https://fonts.googleapis.com/css2?family=Recursive&display=swap');

            * {
                font-family: 'Recursive', sans-serif;
            }

            .theme-choice:hover {
                background-color: #08956E;
                transition: 0.5s;
            }
            
            #jumbotron {
                min-height: 100vh;
            }
            
            .btn-donate {
                background-color: #08956E;
            }

            .btn-donate:hover {
                background-color: #1fa37d;
            }

            .social-icon a ion-icon {
                color: inherit;
                padding: 8px;
                margin: 8px;
                background-color: #F8F9FA;
                border-radius: 50%;
                font-size: 20px;
            }

            .social-icon a ion-icon:hover {
                background-color: #08956E;
                transition: 0.5s;
            }

            .jump-top a ion-icon {
                color: inherit;
                padding: 8px;
                margin: 8px;
                background-color: #08956E;
                border-radius: 50%;
                font-size: 20px;
            }
            
            .btn-donate-extra-small-active {
                display: none;
            }

            @media only screen and (max-width:576px) {
                .btn-donate-extra-small {
                    display: none;
                }
                
                .btn-donate-extra-small-active {
                    display: block;
                }
            }
            '''
            ) if is_dark_theme == False else html.style(
                '''
            @import url('https://fonts.googleapis.com/css2?family=Recursive&display=swap');

            * {
                font-family: 'Recursive', sans-serif;
            }

            .theme-choice:hover {
                background-color: #08956E;
                transition: 0.5s;
            }
            
            #jumbotron {
                min-height: 100vh;
            }
            
            .border-konten-donate {
                background-color: #1E293B;
            }
            
            .btn-donate {
                background-color: #08956E;
            }

            .btn-donate:hover {
                background-color: #1fa37d;
            }

            .social-icon a ion-icon {
                color: inherit;
                padding: 8px;
                margin: 8px;
                background-color: #F8F9FA;
                border-radius: 50%;
                font-size: 20px;
            }

            .social-icon a ion-icon:hover {
                background-color: #08956E;
                transition: 0.5s;
            }

            .jump-top a ion-icon {
                color: inherit;
                padding: 8px;
                margin: 8px;
                background-color: #08956E;
                border-radius: 50%;
                font-size: 20px;
            }
            
            .btn-donate-extra-small-active {
                display: none;
            }

            @media only screen and (max-width:576px) {
                .btn-donate-extra-small {
                    display: none;
                }
                
                .btn-donate-extra-small-active {
                    display: block;
                }
            }
            '''
            ),
            html.nav(
                {
                    'class_name': 'navbar navbar-expand-lg navbar-dark shadow-sm fixed-top',
                    'style': {
                        'background-color': '#4C5264'
                    }
                },
                html.div(
                    {
                        'class_name': 'container'
                    },
                    html.a(
                        {
                            'class_name': 'navbar-brand fw-bold',
                            'href': '/donation#',
                        },
                        html.img(
                            {
                                'src': '../../../static/image/rps-api-icon.png',
                                'style': {
                                    'width': '50px',
                                    'height': '50px'
                                },
                            }
                        ),
                        html.span(
                            {
                                'class_name': 'ms-3'
                            },
                            'Ditttt RPS API'
                        )
                    ),
                    html.button(
                        {
                            'class_name': 'navbar-toggler',
                            'type': 'button',
                            'data-bs-toggle': 'collapse',
                            'data-bs-target': '#navbarNav',
                            'aria-controls': 'navbarNav',
                            'aria-expanded': 'false',
                            'aria-label': 'Toggle navigation'
                        },
                        html.span(
                            {
                                'class_name': 'navbar-toggler-icon'
                            }
                        )
                    ),
                    html.div(
                        {
                            'class_name': 'collapse navbar-collapse',
                            'id': 'navbarNav'
                        },
                        html.ul(
                            {
                                'class_name': 'navbar-nav ms-auto fw-bold'
                            },
                            html.li(
                                {
                                    'class_name': 'nav-item'
                                },
                                html.a(
                                    {
                                        'class_name': 'nav-link',
                                        'aria-current': 'page',
                                        'href': '/',
                                        'style': {
                                            'color': f'#D5E7FF' if location.pathname == '/' else ''
                                        }
                                    },
                                    html.i(
                                        {
                                            'class_name': f'fa-solid fa-home',
                                        },
                                    ),
                                    ' Docs'
                                )
                            ),
                            html.li(
                                {
                                    'class_name': 'nav-item'
                                },
                                html.a(
                                    {
                                        'class_name': 'nav-link',
                                        'aria-current': 'page',
                                        'href': '/contact',
                                        'style': {
                                            'color': f'#D5E7FF' if location.pathname == '/contact' else ''
                                        }
                                    },
                                    html.i(
                                        {
                                            'class_name': f'fa-solid fa-envelope'
                                        },
                                    ),
                                    ' Contact'
                                )
                            ),
                            html.li(
                                {
                                    'class_name': 'nav-item'
                                },
                                html.a(
                                    {
                                        'class_name': 'nav-link',
                                        'aria-current': 'page',
                                        'href': '/donation',
                                        'style': {
                                            'color': f'#D5E7FF' if location.pathname == '/donation' else ''
                                        }
                                    },
                                    html.i(
                                        {
                                            'class_name': f'fa-solid fa-money-bill'
                                        },
                                    ),
                                    ' Donation'
                                )
                            ),
                            html.li(
                                {
                                    'class_name': 'nav-item dropdown'
                                },
                                html.button(
                                    {
                                        'class_name': 'btn nav-link dropdown-toggle',
                                        'type': 'button',
                                        'data-bs-toggle': 'dropdown',
                                        'aria-expanded': 'false',
                                        'on_click': toggle_dropdown_theme
                                    },
                                    html.i(
                                        {
                                            'class_name': f'bi bi-{"moon" if is_dark_theme else "sun"}-fill me-1'
                                        },
                                    ),
                                ),
                                html.ul(
                                    {
                                        'class_name': f'dropdown-menu dropdown-menu-end'
                                    },
                                    html.li(
                                        {
                                            'style': {
                                                'background-color': '#4C5264' if is_dark_theme == True else ''
                                            }
                                        },
                                        html.a(
                                            {
                                                'class_name': f'{"theme-choice" if is_dark_theme == False else "disabled"} {"text-light" if is_dark_theme == True else "text-dark"} dropdown-item d-flex align-items-center',
                                                'href': '#',
                                                'on_click': lambda event: handle_option_click_theme(html.i(
                                                    {
                                                        'class_name': 'bi bi-moon-fill'
                                                    }
                                                ), True)
                                            },
                                            html.span(
                                                {
                                                    'class_name': 'd-flex',
                                                },
                                                html.i(
                                                    {
                                                        'class_name': f'bi bi-moon-fill me-2'
                                                    },
                                                ),
                                                'Dark',
                                                html.i(
                                                    {
                                                        'class_name': f'bi bi-check2 ms-2'
                                                    },
                                                ) if is_dark_theme == True else '',
                                            )
                                        )
                                    ),
                                    html.li(
                                        {
                                            'style': {
                                                'background-color': '#4C5264' if is_dark_theme == False else ''
                                            }
                                        },
                                        html.a(
                                            {
                                                'class_name': f'{"theme-choice" if is_dark_theme == True else "disabled"} {"text-light" if is_dark_theme == False else "text-dark"} dropdown-item d-flex align-items-center',
                                                'href': '#',
                                                'on_click': lambda event: handle_option_click_theme(html.i(
                                                    {
                                                        'class_name': 'bi bi-sun-fill'
                                                    }
                                                ), False)
                                            },
                                            html.span(
                                                {
                                                    'class_name': 'd-flex',
                                                },
                                                html.i(
                                                    {
                                                        'class_name': f'bi bi-sun-fill me-2'
                                                    },
                                                ),
                                                'Light',
                                                html.i(
                                                    {
                                                        'class_name': f'bi bi-check2 ms-2'
                                                    },
                                                ) if is_dark_theme == False else '',
                                            )
                                        )
                                    ),
                                    html.li(
                                        html.a(
                                            {
                                                'class_name': f'theme-choice dropdown-item d-flex align-items-center',
                                                'href': '#',
                                                'on_click': lambda event: handle_option_click_theme(html.i(
                                                    {
                                                        'class_name': f'bi bi-{"sun" if is_dark_theme == False else "moon"}-fill'
                                                    }
                                                ), False if is_dark_theme else True)
                                            },
                                            html.i(
                                                {
                                                    'class_name': f'bi bi-circle-half me-2'
                                                },
                                            ),
                                            'Auto'
                                        )
                                    )
                                ),
                            ),
                        ),
                    )
                )
            ),
            component_jumbotron(is_dark_theme),
            component_footer(),
            jump_top('/donation#')
        ) if is_loading == False else preload()
    )
