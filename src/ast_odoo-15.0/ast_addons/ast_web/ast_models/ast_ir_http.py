Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='hashlib', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='http', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='file_open', asname=None),
                alias(name='image_process', asname=None),
                alias(name='ustr', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.web.controllers.main',
            names=[alias(name='HomeStaticTemplateHelpers', asname=None)],
            level=0,
        ),
        ClassDef(
            name='Http',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.http', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='webclient_rendering_context',
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
                                    Constant(value='menu_data', kind=None),
                                    Constant(value='session_info', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.ui.menu', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='load_menus',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='session',
                                                    ctx=Load(),
                                                ),
                                                attr='debug',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='session_info',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
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
                    name='session_info',
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
                            targets=[Name(id='user', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='user',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='version_info', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='service',
                                            ctx=Load(),
                                        ),
                                        attr='common',
                                        ctx=Load(),
                                    ),
                                    attr='exp_version',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='session_uid', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='session',
                                    ctx=Load(),
                                ),
                                attr='uid',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user_context', ctx=Store())],
                            value=IfExp(
                                test=Name(id='session_uid', ctx=Load()),
                                body=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='session',
                                            ctx=Load(),
                                        ),
                                        attr='get_context',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                orelse=Dict(keys=[], values=[]),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='IrConfigSudo', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.config_parameter', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='max_file_upload_size', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='IrConfigSudo', ctx=Load()),
                                            attr='get_param',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='web.max_file_upload_size', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='default',
                                                value=BinOp(
                                                    left=BinOp(
                                                        left=Constant(value=128, kind=None),
                                                        op=Mult(),
                                                        right=Constant(value=1024, kind=None),
                                                    ),
                                                    op=Mult(),
                                                    right=Constant(value=1024, kind=None),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mods', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='conf',
                                            ctx=Load(),
                                        ),
                                        attr='server_wide_modules',
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lang', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='user_context', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='lang', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='translation_hash', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.translation', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get_web_translations_hash',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='mods', ctx=Load()),
                                    Name(id='lang', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='session_info', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='uid', kind=None),
                                    Constant(value='is_system', kind=None),
                                    Constant(value='is_admin', kind=None),
                                    Constant(value='user_context', kind=None),
                                    Constant(value='db', kind=None),
                                    Constant(value='server_version', kind=None),
                                    Constant(value='server_version_info', kind=None),
                                    Constant(value='support_url', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='username', kind=None),
                                    Constant(value='partner_display_name', kind=None),
                                    Constant(value='company_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='web.base.url', kind=None),
                                    Constant(value='active_ids_limit', kind=None),
                                    Constant(value='profile_session', kind=None),
                                    Constant(value='profile_collectors', kind=None),
                                    Constant(value='profile_params', kind=None),
                                    Constant(value='max_file_upload_size', kind=None),
                                    Constant(value='home_action_id', kind=None),
                                    Constant(value='cache_hashes', kind=None),
                                    Constant(value='currencies', kind=None),
                                ],
                                values=[
                                    Name(id='session_uid', ctx=Load()),
                                    IfExp(
                                        test=Name(id='session_uid', ctx=Load()),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='user', ctx=Load()),
                                                attr='_is_system',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        orelse=Constant(value=False, kind=None),
                                    ),
                                    IfExp(
                                        test=Name(id='session_uid', ctx=Load()),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='user', ctx=Load()),
                                                attr='_is_admin',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        orelse=Constant(value=False, kind=None),
                                    ),
                                    Name(id='user_context', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='session',
                                            ctx=Load(),
                                        ),
                                        attr='db',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='version_info', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='server_version', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='version_info', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='server_version_info', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='https://www.odoo.com/buy', kind=None),
                                    Attribute(
                                        value=Name(id='user', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='user', ctx=Load()),
                                        attr='login',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='user', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='display_name',
                                        ctx=Load(),
                                    ),
                                    IfExp(
                                        test=Name(id='session_uid', ctx=Load()),
                                        body=Attribute(
                                            value=Attribute(
                                                value=Name(id='user', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        orelse=Constant(value=None, kind=None),
                                    ),
                                    IfExp(
                                        test=BoolOp(
                                            op=And(),
                                            values=[
                                                Name(id='session_uid', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='user', ctx=Load()),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        body=Attribute(
                                            value=Attribute(
                                                value=Name(id='user', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        orelse=Constant(value=None, kind=None),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='IrConfigSudo', ctx=Load()),
                                            attr='get_param',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='web.base.url', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='default',
                                                value=Constant(value='', kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='IrConfigSudo', ctx=Load()),
                                                    attr='get_param',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='web.active_ids_limit', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='default',
                                                        value=Constant(value='20000', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='session',
                                            ctx=Load(),
                                        ),
                                        attr='profile_session',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='session',
                                            ctx=Load(),
                                        ),
                                        attr='profile_collectors',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='session',
                                            ctx=Load(),
                                        ),
                                        attr='profile_params',
                                        ctx=Load(),
                                    ),
                                    Name(id='max_file_upload_size', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='user', ctx=Load()),
                                            attr='action_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='translations', kind=None)],
                                        values=[Name(id='translation_hash', ctx=Load())],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='get_currencies',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='has_group',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.group_user', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='db',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='mods', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Name(id='list', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='registry',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_init_modules',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Name(id='mods', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='qweb_checksum', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='HomeStaticTemplateHelpers', ctx=Load()),
                                            attr='get_qweb_templates_checksum',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='debug',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='session',
                                                        ctx=Load(),
                                                    ),
                                                    attr='debug',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='bundle',
                                                value=Constant(value='web.assets_qweb', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='menus', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.ui.menu', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='load_menus',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='session',
                                                    ctx=Load(),
                                                ),
                                                attr='debug',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='ordered_menus', ctx=Store())],
                                    value=DictComp(
                                        key=Call(
                                            func=Name(id='str', ctx=Load()),
                                            args=[Name(id='k', ctx=Load())],
                                            keywords=[],
                                        ),
                                        value=Name(id='v', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='k', ctx=Store()),
                                                        Name(id='v', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='menus', ctx=Load()),
                                                        attr='items',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='menu_json_utf8', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='json', ctx=Load()),
                                                    attr='dumps',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='ordered_menus', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='default',
                                                        value=Name(id='ustr', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='sort_keys',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='encode',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='session_info', ctx=Load()),
                                                slice=Constant(value='cache_hashes', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='load_menus', kind=None),
                                                    Constant(value='qweb', kind=None),
                                                ],
                                                values=[
                                                    Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='hashlib', ctx=Load()),
                                                                        attr='sha512',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Name(id='menu_json_utf8', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                attr='hexdigest',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        slice=Slice(
                                                            lower=None,
                                                            upper=Constant(value=64, kind=None),
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='qweb_checksum', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='session_info', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='user_companies', kind=None),
                                                    Constant(value='show_effect', kind=None),
                                                    Constant(value='display_switch_company_menu', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='current_company', kind=None),
                                                            Constant(value='allowed_companies', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='user', ctx=Load()),
                                                                    attr='company_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            DictComp(
                                                                key=Attribute(
                                                                    value=Name(id='comp', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                value=Dict(
                                                                    keys=[
                                                                        Constant(value='id', kind=None),
                                                                        Constant(value='name', kind=None),
                                                                    ],
                                                                    values=[
                                                                        Attribute(
                                                                            value=Name(id='comp', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='comp', ctx=Load()),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Name(id='comp', ctx=Store()),
                                                                        iter=Attribute(
                                                                            value=Name(id='user', ctx=Load()),
                                                                            attr='company_ids',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ifs=[],
                                                                        is_async=0,
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    Constant(value=True, kind=None),
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='user', ctx=Load()),
                                                                    attr='has_group',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='base.group_multi_company', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            Compare(
                                                                left=Call(
                                                                    func=Name(id='len', ctx=Load()),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='user', ctx=Load()),
                                                                            attr='company_ids',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                ops=[Gt()],
                                                                comparators=[Constant(value=1, kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='session_info', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_frontend_session_info',
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
                            targets=[Name(id='session_info', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='is_admin', kind=None),
                                    Constant(value='is_system', kind=None),
                                    Constant(value='is_website_user', kind=None),
                                    Constant(value='user_id', kind=None),
                                    Constant(value='is_frontend', kind=None),
                                    Constant(value='profile_session', kind=None),
                                    Constant(value='profile_collectors', kind=None),
                                    Constant(value='profile_params', kind=None),
                                    Constant(value='show_effect', kind=None),
                                ],
                                values=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='session',
                                                            ctx=Load(),
                                                        ),
                                                        attr='uid',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='user',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_is_admin',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='session',
                                                            ctx=Load(),
                                                        ),
                                                        attr='uid',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='user',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_is_system',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='session',
                                                            ctx=Load(),
                                                        ),
                                                        attr='uid',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='user',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_is_public',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='session',
                                                            ctx=Load(),
                                                        ),
                                                        attr='uid',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='user',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Constant(value=True, kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='session',
                                            ctx=Load(),
                                        ),
                                        attr='profile_session',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='session',
                                            ctx=Load(),
                                        ),
                                        attr='profile_collectors',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='session',
                                            ctx=Load(),
                                        ),
                                        attr='profile_params',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.config_parameter', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='get_param',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='base_setup.show_effect', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='session',
                                    ctx=Load(),
                                ),
                                attr='uid',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='version_info', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='odoo', ctx=Load()),
                                                    attr='service',
                                                    ctx=Load(),
                                                ),
                                                attr='common',
                                                ctx=Load(),
                                            ),
                                            attr='exp_version',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='session_info', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='server_version', kind=None),
                                                    Constant(value='server_version_info', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='version_info', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='server_version', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='version_info', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='server_version_info', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='session_info', ctx=Load()),
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
                    name='get_currencies',
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
                            targets=[Name(id='Currency', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.currency', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='currencies', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Currency', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='read',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='symbol', kind=None),
                                            Constant(value='position', kind=None),
                                            Constant(value='decimal_places', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=DictComp(
                                key=Subscript(
                                    value=Name(id='c', ctx=Load()),
                                    slice=Constant(value='id', kind=None),
                                    ctx=Load(),
                                ),
                                value=Dict(
                                    keys=[
                                        Constant(value='symbol', kind=None),
                                        Constant(value='position', kind=None),
                                        Constant(value='digits', kind=None),
                                    ],
                                    values=[
                                        Subscript(
                                            value=Name(id='c', ctx=Load()),
                                            slice=Constant(value='symbol', kind=None),
                                            ctx=Load(),
                                        ),
                                        Subscript(
                                            value=Name(id='c', ctx=Load()),
                                            slice=Constant(value='position', kind=None),
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[
                                                Constant(value=69, kind=None),
                                                Subscript(
                                                    value=Name(id='c', ctx=Load()),
                                                    slice=Constant(value='decimal_places', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='c', ctx=Store()),
                                        iter=Name(id='currencies', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
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
                    name='_get_content_common',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='xmlid', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='res_id', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='unique', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                            arg(arg='filename_field', annotation=None, type_comment=None),
                            arg(arg='download', annotation=None, type_comment=None),
                            arg(arg='mimetype', annotation=None, type_comment=None),
                            arg(arg='access_token', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value='ir.attachment', kind=None),
                            Constant(value=None, kind=None),
                            Constant(value='datas', kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value='name', kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='status', ctx=Store()),
                                        Name(id='headers', ctx=Store()),
                                        Name(id='content', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='binary_content',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='xmlid',
                                        value=Name(id='xmlid', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='model',
                                        value=Name(id='model', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='id',
                                        value=Name(id='res_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='field',
                                        value=Name(id='field', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='unique',
                                        value=Name(id='unique', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='filename',
                                        value=Name(id='filename', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='filename_field',
                                        value=Name(id='filename_field', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='download',
                                        value=Name(id='download', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='mimetype',
                                        value=Name(id='mimetype', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='access_token',
                                        value=Name(id='access_token', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='status', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Constant(value=200, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_response_by_status',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='status', ctx=Load()),
                                            Name(id='headers', ctx=Load()),
                                            Name(id='content', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='content_base64', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='base64', ctx=Load()),
                                            attr='b64decode',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='content', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='headers', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='Content-Length', kind=None),
                                                    Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[Name(id='content_base64', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='response', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='make_response',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='content_base64', ctx=Load()),
                                            Name(id='headers', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='response', ctx=Load()),
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
                    name='_content_image',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='xmlid', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='res_id', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='filename_field', annotation=None, type_comment=None),
                            arg(arg='unique', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                            arg(arg='mimetype', annotation=None, type_comment=None),
                            arg(arg='download', annotation=None, type_comment=None),
                            arg(arg='width', annotation=None, type_comment=None),
                            arg(arg='height', annotation=None, type_comment=None),
                            arg(arg='crop', annotation=None, type_comment=None),
                            arg(arg='quality', annotation=None, type_comment=None),
                            arg(arg='access_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value='ir.attachment', kind=None),
                            Constant(value=None, kind=None),
                            Constant(value='datas', kind=None),
                            Constant(value='name', kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=0, kind=None),
                            Constant(value=0, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=0, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='status', ctx=Store()),
                                        Name(id='headers', ctx=Store()),
                                        Name(id='image_base64', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='binary_content',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='xmlid',
                                        value=Name(id='xmlid', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='model',
                                        value=Name(id='model', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='id',
                                        value=Name(id='res_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='field',
                                        value=Name(id='field', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='unique',
                                        value=Name(id='unique', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='filename',
                                        value=Name(id='filename', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='filename_field',
                                        value=Name(id='filename_field', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='download',
                                        value=Name(id='download', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='mimetype',
                                        value=Name(id='mimetype', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='default_mimetype',
                                        value=Constant(value='image/png', kind=None),
                                    ),
                                    keyword(
                                        arg='access_token',
                                        value=Name(id='access_token', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_content_image_get_response',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='status', ctx=Load()),
                                    Name(id='headers', ctx=Load()),
                                    Name(id='image_base64', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='model',
                                        value=Name(id='model', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='field',
                                        value=Name(id='field', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='download',
                                        value=Name(id='download', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='width',
                                        value=Name(id='width', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='height',
                                        value=Name(id='height', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='crop',
                                        value=Name(id='crop', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='quality',
                                        value=Name(id='quality', ctx=Load()),
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
                    name='_content_image_get_response',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='status', annotation=None, type_comment=None),
                            arg(arg='headers', annotation=None, type_comment=None),
                            arg(arg='image_base64', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='download', annotation=None, type_comment=None),
                            arg(arg='width', annotation=None, type_comment=None),
                            arg(arg='height', annotation=None, type_comment=None),
                            arg(arg='crop', annotation=None, type_comment=None),
                            arg(arg='quality', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value='ir.attachment', kind=None),
                            Constant(value='datas', kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=0, kind=None),
                            Constant(value=0, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=0, kind=None),
                        ],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Name(id='status', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value=301, kind=None),
                                                    Constant(value=304, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='status', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Constant(value=200, kind=None)],
                                            ),
                                            Name(id='download', ctx=Load()),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_response_by_status',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='status', ctx=Load()),
                                            Name(id='headers', ctx=Load()),
                                            Name(id='image_base64', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='image_base64', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='placeholder_filename', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='model', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='placeholder_filename', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Name(id='model', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_get_placeholder_filename',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='field', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='placeholder_content', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_placeholder',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='image',
                                                value=Name(id='placeholder_filename', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='status', ctx=Store())],
                                    value=Constant(value=200, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='image_base64', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='base64', ctx=Load()),
                                            attr='b64encode',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='placeholder_content', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=BoolOp(
                                            op=Or(),
                                            values=[
                                                Name(id='width', ctx=Load()),
                                                Name(id='height', ctx=Load()),
                                            ],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='width', ctx=Store()),
                                                        Name(id='height', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='odoo', ctx=Load()),
                                                        attr='tools',
                                                        ctx=Load(),
                                                    ),
                                                    attr='image_guess_size_from_field_name',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='field', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='image_base64', ctx=Store())],
                                    value=Call(
                                        func=Name(id='image_process', ctx=Load()),
                                        args=[Name(id='image_base64', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='size',
                                                value=Tuple(
                                                    elts=[
                                                        Call(
                                                            func=Name(id='int', ctx=Load()),
                                                            args=[Name(id='width', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        Call(
                                                            func=Name(id='int', ctx=Load()),
                                                            args=[Name(id='height', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='crop',
                                                value=Name(id='crop', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='quality',
                                                value=Call(
                                                    func=Name(id='int', ctx=Load()),
                                                    args=[Name(id='quality', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='not_found',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='base64', ctx=Load()),
                                    attr='b64decode',
                                    ctx=Load(),
                                ),
                                args=[Name(id='image_base64', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='headers', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='http', ctx=Load()),
                                    attr='set_safe_image_headers',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='headers', ctx=Load()),
                                    Name(id='content', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='make_response',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='content', ctx=Load()),
                                    Name(id='headers', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='response', ctx=Load()),
                                    attr='status_code',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='status', ctx=Load()),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='response', ctx=Load()),
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
                    name='_placeholder_image_get_response',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='placeholder_base64', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='base64', ctx=Load()),
                                    attr='b64decode',
                                    ctx=Load(),
                                ),
                                args=[Name(id='placeholder_base64', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='headers', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='http', ctx=Load()),
                                    attr='set_safe_image_headers',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(elts=[], ctx=Load()),
                                    Name(id='content', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='make_response',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='content', ctx=Load()),
                                    Name(id='headers', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='response', ctx=Load()),
                                    attr='status_code',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=200, kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='response', ctx=Load()),
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
                    name='_placeholder',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='image', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='image', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='image', ctx=Store())],
                                    value=Constant(value='web/static/img/placeholder.png', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='file_open', ctx=Load()),
                                        args=[
                                            Name(id='image', ctx=Load()),
                                            Constant(value='rb', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='filter_ext',
                                                value=Tuple(
                                                    elts=[
                                                        Constant(value='.png', kind=None),
                                                        Constant(value='.jpg', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='fd', ctx=Store()),
                                ),
                            ],
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='fd', ctx=Load()),
                                            attr='read',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
