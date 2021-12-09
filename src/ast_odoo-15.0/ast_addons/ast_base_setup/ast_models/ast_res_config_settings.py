Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ClassDef(
            name='ResConfigSettings',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='res.config.settings', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.company', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Company', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='user_default_rights', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Default Access Rights', kind=None)],
                        keywords=[
                            keyword(
                                arg='config_parameter',
                                value=Constant(value='base_setup.default_user_rights', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='external_email_server_default', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Custom Email Servers', kind=None)],
                        keywords=[
                            keyword(
                                arg='config_parameter',
                                value=Constant(value='base_setup.default_external_email_server', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_base_import', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Allow users to import data from CSV/XLS/XLSX/ODS files', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_google_calendar', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Allow the users to synchronize their calendar  with Google Calendar', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_microsoft_calendar', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Allow the users to synchronize their calendar with Outlook Calendar', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_mail_plugin', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Allow integration with the mail plugins', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_google_drive', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Attach Google documents to any record', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_google_spreadsheet', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Google Spreadsheet', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_auth_oauth', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Use external authentication providers (OAuth)', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_auth_ldap', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='LDAP Authentication', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_base_gengo', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Translate Your Website with Gengo', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_account_inter_company_rules', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Manage Inter Company', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_pad', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Collaborative Pads', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_voip', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Asterisk (VoIP)', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_web_unsplash', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Unsplash Image Library', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_partner_autocomplete', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Partner Autocomplete', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_base_geolocalize', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='GeoLocalize', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_google_recaptcha', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='reCAPTCHA', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='report_footer', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Html',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.report_footer', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Custom Report Footer', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Footer text displayed at the bottom of all reports.', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_multi_currency', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Multi-Currencies', kind=None),
                            ),
                            keyword(
                                arg='implied_group',
                                value=Constant(value='base.group_multi_currency', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Allows to work in a multi currency environment', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='external_report_layout_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.external_report_layout_id', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='show_effect', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Show Effect', kind=None),
                            ),
                            keyword(
                                arg='config_parameter',
                                value=Constant(value='base_setup.show_effect', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Number of Companies', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_company_count', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='active_user_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Number of Active Users', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_active_user_count', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='language_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Number of Languages', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_language_count', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.display_name', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Company Name', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_informations', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_company_informations', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='profiling_enabled_until', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Profiling enabled until', kind=None)],
                        keywords=[
                            keyword(
                                arg='config_parameter',
                                value=Constant(value='base.profiling_enabled_until', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_product_images', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Get product pictures using barcode', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='open_company',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='type', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='res_id', kind=None),
                                    Constant(value='target', kind=None),
                                    Constant(value='context', kind=None),
                                ],
                                values=[
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Constant(value='My Company', kind=None),
                                    Constant(value='form', kind=None),
                                    Constant(value='res.company', kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='current', kind=None),
                                    Dict(
                                        keys=[Constant(value='form_view_initial_mode', kind=None)],
                                        values=[Constant(value='edit', kind=None)],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='open_default_user',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.actions.actions', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_for_xml_id',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.action_res_users', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.default_user', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='raise_if_not_found',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='action', ctx=Load()),
                                            slice=Constant(value='res_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='ref',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='base.default_user', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Default User Template not found.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='action', ctx=Load()),
                                    slice=Constant(value='views', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ref',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='base.view_users_form', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='form', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='action', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_report_view_action',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='template', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='template_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Name(id='template', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='type', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='res_id', kind=None),
                                ],
                                values=[
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Constant(value='ir.ui.view', kind=None),
                                    Constant(value='form', kind=None),
                                    Attribute(
                                        value=Name(id='template_id', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='edit_external_header',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='external_report_layout_id',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_report_view_action',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='external_report_layout_id',
                                            ctx=Load(),
                                        ),
                                        attr='key',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_company_count',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='company_count', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.company', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search_count',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='company_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='company_count', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='company_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_active_user_count',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='active_user_count', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.users', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='share', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='active_user_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='active_user_count', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='company_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_language_count',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='language_count', ctx=Store())],
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.lang', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='get_installed',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='language_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='language_count', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='company_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_company_informations',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='informations', ctx=Store())],
                            value=IfExp(
                                test=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    attr='street',
                                    ctx=Load(),
                                ),
                                body=BinOp(
                                    left=Constant(value='%s\n', kind=None),
                                    op=Mod(),
                                    right=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='street',
                                        ctx=Load(),
                                    ),
                                ),
                                orelse=Constant(value='', kind=None),
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Name(id='informations', ctx=Store()),
                            op=Add(),
                            value=IfExp(
                                test=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    attr='street2',
                                    ctx=Load(),
                                ),
                                body=BinOp(
                                    left=Constant(value='%s\n', kind=None),
                                    op=Mod(),
                                    right=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='street2',
                                        ctx=Load(),
                                    ),
                                ),
                                orelse=Constant(value='', kind=None),
                            ),
                        ),
                        AugAssign(
                            target=Name(id='informations', ctx=Store()),
                            op=Add(),
                            value=IfExp(
                                test=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    attr='zip',
                                    ctx=Load(),
                                ),
                                body=BinOp(
                                    left=Constant(value='%s', kind=None),
                                    op=Mod(),
                                    right=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='zip',
                                        ctx=Load(),
                                    ),
                                ),
                                orelse=Constant(value='', kind=None),
                            ),
                        ),
                        AugAssign(
                            target=Name(id='informations', ctx=Store()),
                            op=Add(),
                            value=IfExp(
                                test=BoolOp(
                                    op=And(),
                                    values=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='zip',
                                            ctx=Load(),
                                        ),
                                        UnaryOp(
                                            op=Not(),
                                            operand=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='city',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                                body=Constant(value='\n', kind=None),
                                orelse=Constant(value='', kind=None),
                            ),
                        ),
                        AugAssign(
                            target=Name(id='informations', ctx=Store()),
                            op=Add(),
                            value=IfExp(
                                test=BoolOp(
                                    op=And(),
                                    values=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='zip',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='city',
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                                body=Constant(value=' - ', kind=None),
                                orelse=Constant(value='', kind=None),
                            ),
                        ),
                        AugAssign(
                            target=Name(id='informations', ctx=Store()),
                            op=Add(),
                            value=IfExp(
                                test=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    attr='city',
                                    ctx=Load(),
                                ),
                                body=BinOp(
                                    left=Constant(value='%s\n', kind=None),
                                    op=Mod(),
                                    right=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='city',
                                        ctx=Load(),
                                    ),
                                ),
                                orelse=Constant(value='', kind=None),
                            ),
                        ),
                        AugAssign(
                            target=Name(id='informations', ctx=Store()),
                            op=Add(),
                            value=IfExp(
                                test=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    attr='state_id',
                                    ctx=Load(),
                                ),
                                body=BinOp(
                                    left=Constant(value='%s\n', kind=None),
                                    op=Mod(),
                                    right=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='state_id',
                                            ctx=Load(),
                                        ),
                                        attr='display_name',
                                        ctx=Load(),
                                    ),
                                ),
                                orelse=Constant(value='', kind=None),
                            ),
                        ),
                        AugAssign(
                            target=Name(id='informations', ctx=Store()),
                            op=Add(),
                            value=IfExp(
                                test=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    attr='country_id',
                                    ctx=Load(),
                                ),
                                body=BinOp(
                                    left=Constant(value='%s', kind=None),
                                    op=Mod(),
                                    right=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='country_id',
                                            ctx=Load(),
                                        ),
                                        attr='display_name',
                                        ctx=Load(),
                                    ),
                                ),
                                orelse=Constant(value='', kind=None),
                            ),
                        ),
                        AugAssign(
                            target=Name(id='informations', ctx=Store()),
                            op=Add(),
                            value=IfExp(
                                test=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    attr='vat',
                                    ctx=Load(),
                                ),
                                body=BinOp(
                                    left=Constant(value='\nVAT: %s', kind=None),
                                    op=Mod(),
                                    right=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='vat',
                                        ctx=Load(),
                                    ),
                                ),
                                orelse=Constant(value='', kind=None),
                            ),
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='company_informations',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='informations', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='company_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
