from reactpy.core.component import Component
from reactpy import component, html, use_state, event
import requests
from email.message import EmailMessage
import ssl
import smtplib
from dotenv import load_dotenv
import os
import traceback
from ...misc import Misc


@component
def contact_form(is_dark_theme) -> Component:
    load_dotenv()

    email, set_email = use_state('')
    name, set_name = use_state('')
    message, set_message = use_state('')

    email_error, set_email_error = use_state('')
    name_error, set_name_error = use_state('')
    message_error, set_message_error = use_state('')

    klik, set_klik = use_state(False)

    def handle_click_off(event: dict):
        set_klik(False)

    def handle_message(event: dict):
        value = event['target']['value']
        set_message(value)

    def handle_name(event: dict):
        value = event['target']['value']
        set_name(value)

    def handle_email(event: dict):
        value = event['target']['value']
        set_email(value)

    def handle_submit(event: dict):
        inputan_kosong = Misc.cek_inputan(email, name, message)
        if not inputan_kosong:
            try:
                if (valid_email := Misc.check_email(email))['valid'] == True:
                    Misc.send_email(email, name, message)
                    set_klik(True)
                    set_email('')
                    set_email_error('')
                    set_name('')
                    set_name_error('')
                    set_message('')
                    set_message_error('')
                    return
                else:
                    set_email_error(f'email {email} not valid'.title())
                    return
            except:
                traceback.print_exc()
        elif len(inputan_kosong) > 0 and len(inputan_kosong) < 3:
            value = ['email', 'name', 'message']
            missing_elements = list(set(value) - set(inputan_kosong))
            result = list(set(value) - set(missing_elements))
            print(result)
            for i in result:
                if i == 'email':
                    set_email_error(f'name cannot be empty'.title())
                elif i == 'name':
                    set_name_error(f'name cannot be empty'.title())
                else:
                    set_message_error(f'message cannot be empty'.title())
        else:
            value = ['email', 'name', 'message']
            for i in value:
                result = Misc.get_array_item_by_value(inputan_kosong, i)
                if result is not None:
                    if i == 'email':
                        set_email_error(f'email cannot be empty'.title())
                    elif i == 'name':
                        set_name_error(f'name cannot be empty'.title())
                    else:
                        set_message_error(f'message cannot be empty'.title())
            return

    return html._(
        html.div(
            {
                'class_name': 'alert alert-success alert-dismissible fade show mt-3',
                'role': 'alert',
                'style': {
                    'margin-right': '60%'
                }
            },
            html.i(
                {
                    'class_name': 'fa-solid fa-check'
                },
            ),
            ' Success Send Email',
            html.button(
                {
                    'type': 'button',
                    'class_name': 'btn-close',
                    'on_click': handle_click_off,
                }
            )
        ) if klik else '',
        html.form(
            {
                'class_name': 'mb-3',
            },
            html.div(
                {
                    'class_name': 'mb-3'
                },
                html.label(
                    {
                        'for': 'email-input',
                        'class_name': f'form-label judul judul-2 {"text-light" if is_dark_theme else "text-dark"}',
                    },
                    'Email address'.title(),
                ),
                ('' if email_error == '' else html.p(
                    {
                        'class_name': 'text-danger',
                        'style': {
                            'font-size': '12px'
                        }
                    },
                    html.i(
                        {
                            'class_name': 'fa-solid fa-circle-exclamation'
                        }
                    ),
                    f' {email_error}'
                )),
                html.input(
                    {
                        'type': 'email',
                        'class_name': 'form-control',
                        'id': 'email-input',
                        'aria-describedby': 'emailHelp',
                        'value': email,
                        'onchange': handle_email
                    }
                )
            ),
            html.div(
                {
                    'class_name': 'mb-3'
                },
                html.label(
                    {
                        'for': 'name-input',
                        'class_name': f'form-label judul judul-2 {"text-light" if is_dark_theme else "text-dark"}',
                    },
                    'Name'.title(),
                ),
                ('' if name_error == '' else html.p(
                    {
                        'class_name': 'text-danger',
                        'style': {
                            'font-size': '12px'
                        }
                    },
                    html.i(
                        {
                            'class_name': 'fa-solid fa-circle-exclamation'
                        }
                    ),
                    f' {name_error}'
                )),
                html.input(
                    {
                        'type': 'text',
                        'id': 'name-input',
                        'class_name': 'form-control',
                        'aria-describedby': 'passwordHelpBlock',
                        'value': name,
                        'onchange': handle_name
                    }
                )
            ),
            html.div(
                {
                    'class_name': 'mb-3'
                },
                html.label(
                    {
                        'for': 'message-input',
                        'class_name': f'form-label judul judul-2 {"text-light" if is_dark_theme else "text-dark"}',
                    },
                    'Message'.title(),
                ),
                ('' if message_error == '' else html.p(
                    {
                        'class_name': 'text-danger',
                        'style': {
                            'font-size': '12px'
                        }
                    },
                    html.i(
                        {
                            'class_name': 'fa-solid fa-circle-exclamation'
                        }
                    ),
                    f' {message_error}'
                )),
                html.textarea(
                    {
                        'class_name': 'form-control',
                        'id': 'message-input',
                        'rows': '3',
                        'value': message,
                        'onchange': handle_message
                    }
                )
            ),
            html.button(
                {
                    'type': 'button',
                    'class_name': 'btn btn-contact-form',
                    'on_click': handle_submit,
                },
                'Submit',
            )
        )
    )
