Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='shutil', asname=None)],
        ),
        Import(
            names=[alias(name='tempfile', asname=None)],
        ),
        Import(
            names=[alias(name='threading', asname=None)],
        ),
        Import(
            names=[alias(name='traceback', asname=None)],
        ),
        ImportFrom(
            module='xml.etree',
            names=[alias(name='ElementTree', asname='ET')],
            level=0,
        ),
        Import(
            names=[alias(name='zipfile', asname=None)],
        ),
        ImportFrom(
            module='psycopg2',
            names=[alias(name='sql', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='pytz',
            names=[alias(name='country_timezones', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='functools',
            names=[alias(name='wraps', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='contextlib',
            names=[alias(name='closing', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='decorator',
            names=[alias(name='decorator', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='psycopg2', asname=None)],
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='SUPERUSER_ID', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='AccessDenied', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='odoo.release', asname=None)],
        ),
        Import(
            names=[alias(name='odoo.sql_db', asname=None)],
        ),
        Import(
            names=[alias(name='odoo.tools', asname=None)],
        ),
        ImportFrom(
            module='odoo.sql_db',
            names=[alias(name='db_connect', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.release',
            names=[alias(name='version_info', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='DatabaseExists',
            bases=[Name(id='Warning', ctx=Load())],
            keywords=[],
            body=[Pass()],
            decorator_list=[],
        ),
        FunctionDef(
            name='check_db_management_enabled',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='method', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                FunctionDef(
                    name='if_db_mgt_enabled',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='method', annotation=None, type_comment=None),
                            arg(arg='self', annotation=None, type_comment=None),
                        ],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Subscript(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='tools',
                                            ctx=Load(),
                                        ),
                                        attr='config',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='list_db', kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='error',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='Database management functions blocked, admin disabled database listing', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id='AccessDenied', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='method', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Starred(
                                        value=Name(id='args', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Name(id='decorator', ctx=Load()),
                        args=[
                            Name(id='if_db_mgt_enabled', ctx=Load()),
                            Name(id='method', ctx=Load()),
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
            name='check_super',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='passwd', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Name(id='passwd', ctx=Load()),
                            Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='tools',
                                            ctx=Load(),
                                        ),
                                        attr='config',
                                        ctx=Load(),
                                    ),
                                    attr='verify_admin_password',
                                    ctx=Load(),
                                ),
                                args=[Name(id='passwd', ctx=Load())],
                                keywords=[],
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Raise(
                    exc=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='exceptions',
                                ctx=Load(),
                            ),
                            attr='AccessDenied',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    cause=None,
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_initialize_db',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='id', annotation=None, type_comment=None),
                    arg(arg='db_name', annotation=None, type_comment=None),
                    arg(arg='demo', annotation=None, type_comment=None),
                    arg(arg='lang', annotation=None, type_comment=None),
                    arg(arg='user_password', annotation=None, type_comment=None),
                    arg(arg='login', annotation=None, type_comment=None),
                    arg(arg='country_code', annotation=None, type_comment=None),
                    arg(arg='phone', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value='admin', kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                Try(
                    body=[
                        Assign(
                            targets=[Name(id='db', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='sql_db',
                                        ctx=Load(),
                                    ),
                                    attr='db_connect',
                                    ctx=Load(),
                                ),
                                args=[Name(id='db_name', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='closing', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='db', ctx=Load()),
                                                    attr='cursor',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='cr', ctx=Store()),
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='odoo', ctx=Load()),
                                                    attr='modules',
                                                    ctx=Load(),
                                                ),
                                                attr='db',
                                                ctx=Load(),
                                            ),
                                            attr='initialize',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='cr', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='odoo', ctx=Load()),
                                                    attr='tools',
                                                    ctx=Load(),
                                                ),
                                                attr='config',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='load_language', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='lang', ctx=Load()),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='commit',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='registry', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='modules',
                                                ctx=Load(),
                                            ),
                                            attr='registry',
                                            ctx=Load(),
                                        ),
                                        attr='Registry',
                                        ctx=Load(),
                                    ),
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='db_name', ctx=Load()),
                                    Name(id='demo', ctx=Load()),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='update_module',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='closing', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='registry', ctx=Load()),
                                                    attr='cursor',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='cr', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='env', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='api',
                                                ctx=Load(),
                                            ),
                                            attr='Environment',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='cr', ctx=Load()),
                                            Name(id='SUPERUSER_ID', ctx=Load()),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='lang', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='modules', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='env', ctx=Load()),
                                                        slice=Constant(value='ir.module.module', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='state', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value='installed', kind=None),
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
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='modules', ctx=Load()),
                                                    attr='_update_translations',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='lang', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Name(id='country_code', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='country', ctx=Store())],
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='env', ctx=Load()),
                                                            slice=Constant(value='res.country', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='search',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        List(
                                                            elts=[
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='code', kind=None),
                                                                        Constant(value='ilike', kind=None),
                                                                        Name(id='country_code', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='env', ctx=Load()),
                                                                slice=Constant(value='res.company', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=1, kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='country_id', kind=None),
                                                            Constant(value='currency_id', kind=None),
                                                        ],
                                                        values=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='country_code', ctx=Load()),
                                                                    Attribute(
                                                                        value=Name(id='country', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='country_code', ctx=Load()),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='country', ctx=Load()),
                                                                            attr='currency_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='country_timezones', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Name(id='country_code', ctx=Load()),
                                                                List(elts=[], ctx=Load()),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='users', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='env', ctx=Load()),
                                                                slice=Constant(value='res.users', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='search',
                                                            ctx=Load(),
                                                        ),
                                                        args=[List(elts=[], ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='users', ctx=Load()),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[Constant(value='tz', kind=None)],
                                                                values=[
                                                                    Subscript(
                                                                        value=Subscript(
                                                                            value=Name(id='country_timezones', ctx=Load()),
                                                                            slice=Name(id='country_code', ctx=Load()),
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value=0, kind=None),
                                                                        ctx=Load(),
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
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Name(id='phone', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='env', ctx=Load()),
                                                                slice=Constant(value='res.company', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=1, kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='phone', kind=None)],
                                                        values=[Name(id='phone', ctx=Load())],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Constant(value='@', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='login', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='env', ctx=Load()),
                                                                slice=Constant(value='res.company', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=1, kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='email', kind=None)],
                                                        values=[Name(id='login', ctx=Load())],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='values', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='password', kind=None),
                                            Constant(value='lang', kind=None),
                                        ],
                                        values=[
                                            Name(id='user_password', ctx=Load()),
                                            Name(id='lang', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='login', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='login', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='login', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='emails', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='odoo', ctx=Load()),
                                                        attr='tools',
                                                        ctx=Load(),
                                                    ),
                                                    attr='email_split',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='login', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='emails', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='email', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Name(id='emails', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='env', ctx=Load()),
                                                    attr='ref',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='base.user_admin', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='values', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='SELECT login, password FROM res_users ORDER BY login', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='commit',
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
                    handlers=[
                        ExceptHandler(
                            type=Name(id='Exception', ctx=Load()),
                            name='e',
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='exception',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='CREATE DATABASE failed:', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_create_empty_database',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='name', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='db', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='sql_db',
                                ctx=Load(),
                            ),
                            attr='db_connect',
                            ctx=Load(),
                        ),
                        args=[Constant(value='postgres', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                With(
                    items=[
                        withitem(
                            context_expr=Call(
                                func=Name(id='closing', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='db', ctx=Load()),
                                            attr='cursor',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            optional_vars=Name(id='cr', ctx=Store()),
                        ),
                    ],
                    body=[
                        Assign(
                            targets=[Name(id='chosen_template', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='tools',
                                        ctx=Load(),
                                    ),
                                    attr='config',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='db_template', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='SELECT datname FROM pg_database WHERE datname = %s', kind=None),
                                    Tuple(
                                        elts=[Name(id='name', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='log_exceptions',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='fetchall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='DatabaseExists', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='database %r already exists!', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[Name(id='name', ctx=Load())],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='rollback',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='cr', ctx=Load()),
                                                attr='_cnx',
                                                ctx=Load(),
                                            ),
                                            attr='autocommit',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='collate', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='sql', ctx=Load()),
                                            attr='SQL',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            IfExp(
                                                test=Compare(
                                                    left=Name(id='chosen_template', ctx=Load()),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='template0', kind=None)],
                                                ),
                                                body=Constant(value="LC_COLLATE 'C'", kind=None),
                                                orelse=Constant(value='', kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='sql', ctx=Load()),
                                                            attr='SQL',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value="CREATE DATABASE {} ENCODING 'unicode' {} TEMPLATE {}", kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='format',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='sql', ctx=Load()),
                                                            attr='Identifier',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='name', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Name(id='collate', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='sql', ctx=Load()),
                                                            attr='Identifier',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='chosen_template', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    type_comment=None,
                ),
                If(
                    test=Subscript(
                        value=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='tools',
                                ctx=Load(),
                            ),
                            attr='config',
                            ctx=Load(),
                        ),
                        slice=Constant(value='unaccent', kind=None),
                        ctx=Load(),
                    ),
                    body=[
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='db', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='sql_db',
                                                ctx=Load(),
                                            ),
                                            attr='db_connect',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='name', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='closing', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='db', ctx=Load()),
                                                            attr='cursor',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='cr', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='cr', ctx=Load()),
                                                    attr='execute',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='CREATE EXTENSION IF NOT EXISTS unaccent', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='cr', ctx=Load()),
                                                    attr='commit',
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
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='psycopg2', ctx=Load()),
                                        attr='Error',
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[Pass()],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    orelse=[],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='exp_create_database',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='db_name', annotation=None, type_comment=None),
                    arg(arg='demo', annotation=None, type_comment=None),
                    arg(arg='lang', annotation=None, type_comment=None),
                    arg(arg='user_password', annotation=None, type_comment=None),
                    arg(arg='login', annotation=None, type_comment=None),
                    arg(arg='country_code', annotation=None, type_comment=None),
                    arg(arg='phone', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value='admin', kind=None),
                    Constant(value='admin', kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=' Similar to exp_create but blocking.', kind=None),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='_logger', ctx=Load()),
                            attr='info',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='Create database `%s`.', kind=None),
                            Name(id='db_name', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Name(id='_create_empty_database', ctx=Load()),
                        args=[Name(id='db_name', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Name(id='_initialize_db', ctx=Load()),
                        args=[
                            Name(id='id', ctx=Load()),
                            Name(id='db_name', ctx=Load()),
                            Name(id='demo', ctx=Load()),
                            Name(id='lang', ctx=Load()),
                            Name(id='user_password', ctx=Load()),
                            Name(id='login', ctx=Load()),
                            Name(id='country_code', ctx=Load()),
                            Name(id='phone', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Constant(value=True, kind=None),
                ),
            ],
            decorator_list=[Name(id='check_db_management_enabled', ctx=Load())],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='exp_duplicate_database',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='db_original_name', annotation=None, type_comment=None),
                    arg(arg='db_name', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='_logger', ctx=Load()),
                            attr='info',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='Duplicate database `%s` to `%s`.', kind=None),
                            Name(id='db_original_name', ctx=Load()),
                            Name(id='db_name', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='sql_db',
                                ctx=Load(),
                            ),
                            attr='close_db',
                            ctx=Load(),
                        ),
                        args=[Name(id='db_original_name', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='db', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='sql_db',
                                ctx=Load(),
                            ),
                            attr='db_connect',
                            ctx=Load(),
                        ),
                        args=[Constant(value='postgres', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                With(
                    items=[
                        withitem(
                            context_expr=Call(
                                func=Name(id='closing', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='db', ctx=Load()),
                                            attr='cursor',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            optional_vars=Name(id='cr', ctx=Store()),
                        ),
                    ],
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='cr', ctx=Load()),
                                        attr='_cnx',
                                        ctx=Load(),
                                    ),
                                    attr='autocommit',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='_drop_conn', ctx=Load()),
                                args=[
                                    Name(id='cr', ctx=Load()),
                                    Name(id='db_original_name', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='sql', ctx=Load()),
                                                    attr='SQL',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value="CREATE DATABASE {} ENCODING 'unicode' TEMPLATE {}", kind=None)],
                                                keywords=[],
                                            ),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='sql', ctx=Load()),
                                                    attr='Identifier',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='db_name', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='sql', ctx=Load()),
                                                    attr='Identifier',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='db_original_name', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='registry', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='modules',
                                        ctx=Load(),
                                    ),
                                    attr='registry',
                                    ctx=Load(),
                                ),
                                attr='Registry',
                                ctx=Load(),
                            ),
                            attr='new',
                            ctx=Load(),
                        ),
                        args=[Name(id='db_name', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                With(
                    items=[
                        withitem(
                            context_expr=Call(
                                func=Attribute(
                                    value=Name(id='registry', ctx=Load()),
                                    attr='cursor',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            optional_vars=Name(id='cr', ctx=Store()),
                        ),
                    ],
                    body=[
                        Assign(
                            targets=[Name(id='env', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='api',
                                        ctx=Load(),
                                    ),
                                    attr='Environment',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='cr', ctx=Load()),
                                    Name(id='SUPERUSER_ID', ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='env', ctx=Load()),
                                        slice=Constant(value='ir.config_parameter', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='init',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='force',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='from_fs', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='tools',
                                    ctx=Load(),
                                ),
                                attr='config',
                                ctx=Load(),
                            ),
                            attr='filestore',
                            ctx=Load(),
                        ),
                        args=[Name(id='db_original_name', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='to_fs', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='tools',
                                    ctx=Load(),
                                ),
                                attr='config',
                                ctx=Load(),
                            ),
                            attr='filestore',
                            ctx=Load(),
                        ),
                        args=[Name(id='db_name', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='exists',
                                    ctx=Load(),
                                ),
                                args=[Name(id='from_fs', ctx=Load())],
                                keywords=[],
                            ),
                            UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='path',
                                            ctx=Load(),
                                        ),
                                        attr='exists',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='to_fs', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='shutil', ctx=Load()),
                                    attr='copytree',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='from_fs', ctx=Load()),
                                    Name(id='to_fs', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Constant(value=True, kind=None),
                ),
            ],
            decorator_list=[Name(id='check_db_management_enabled', ctx=Load())],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_drop_conn',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='db_name', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Try(
                    body=[
                        Assign(
                            targets=[Name(id='pid_col', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Attribute(
                                        value=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='_cnx',
                                            ctx=Load(),
                                        ),
                                        attr='server_version',
                                        ctx=Load(),
                                    ),
                                    ops=[GtE()],
                                    comparators=[Constant(value=90200, kind=None)],
                                ),
                                body=Constant(value='pid', kind=None),
                                orelse=Constant(value='procpid', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='SELECT pg_terminate_backend(%(pid_col)s)\n                      FROM pg_stat_activity\n                      WHERE datname = %%s AND\n                            %(pid_col)s != pg_backend_pid()', kind=None),
                                        op=Mod(),
                                        right=Dict(
                                            keys=[Constant(value='pid_col', kind=None)],
                                            values=[Name(id='pid_col', ctx=Load())],
                                        ),
                                    ),
                                    Tuple(
                                        elts=[Name(id='db_name', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='Exception', ctx=Load()),
                            name=None,
                            body=[Pass()],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='exp_drop',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='db_name', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                If(
                    test=Compare(
                        left=Name(id='db_name', ctx=Load()),
                        ops=[NotIn()],
                        comparators=[
                            Call(
                                func=Name(id='list_dbs', ctx=Load()),
                                args=[Constant(value=True, kind=None)],
                                keywords=[],
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='modules',
                                        ctx=Load(),
                                    ),
                                    attr='registry',
                                    ctx=Load(),
                                ),
                                attr='Registry',
                                ctx=Load(),
                            ),
                            attr='delete',
                            ctx=Load(),
                        ),
                        args=[Name(id='db_name', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='sql_db',
                                ctx=Load(),
                            ),
                            attr='close_db',
                            ctx=Load(),
                        ),
                        args=[Name(id='db_name', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='db', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='sql_db',
                                ctx=Load(),
                            ),
                            attr='db_connect',
                            ctx=Load(),
                        ),
                        args=[Constant(value='postgres', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                With(
                    items=[
                        withitem(
                            context_expr=Call(
                                func=Name(id='closing', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='db', ctx=Load()),
                                            attr='cursor',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            optional_vars=Name(id='cr', ctx=Store()),
                        ),
                    ],
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='cr', ctx=Load()),
                                        attr='_cnx',
                                        ctx=Load(),
                                    ),
                                    attr='autocommit',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='_drop_conn', ctx=Load()),
                                args=[
                                    Name(id='cr', ctx=Load()),
                                    Name(id='db_name', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='sql', ctx=Load()),
                                                            attr='SQL',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='DROP DATABASE {}', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='format',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='sql', ctx=Load()),
                                                            attr='Identifier',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='db_name', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='e',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='info',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='DROP DB: %s failed:\n%s', kind=None),
                                                    Name(id='db_name', ctx=Load()),
                                                    Name(id='e', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Raise(
                                            exc=Call(
                                                func=Name(id='Exception', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value="Couldn't drop database %s: %s", kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='db_name', ctx=Load()),
                                                                Name(id='e', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='DROP DB: %s', kind=None),
                                            Name(id='db_name', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            finalbody=[],
                        ),
                    ],
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='fs', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='tools',
                                    ctx=Load(),
                                ),
                                attr='config',
                                ctx=Load(),
                            ),
                            attr='filestore',
                            ctx=Load(),
                        ),
                        args=[Name(id='db_name', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='os', ctx=Load()),
                                attr='path',
                                ctx=Load(),
                            ),
                            attr='exists',
                            ctx=Load(),
                        ),
                        args=[Name(id='fs', ctx=Load())],
                        keywords=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='shutil', ctx=Load()),
                                    attr='rmtree',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fs', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Constant(value=True, kind=None),
                ),
            ],
            decorator_list=[Name(id='check_db_management_enabled', ctx=Load())],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='exp_dump',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='db_name', annotation=None, type_comment=None),
                    arg(arg='format', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                With(
                    items=[
                        withitem(
                            context_expr=Call(
                                func=Attribute(
                                    value=Name(id='tempfile', ctx=Load()),
                                    attr='TemporaryFile',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='mode',
                                        value=Constant(value='w+b', kind=None),
                                    ),
                                ],
                            ),
                            optional_vars=Name(id='t', ctx=Store()),
                        ),
                    ],
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='dump_db', ctx=Load()),
                                args=[
                                    Name(id='db_name', ctx=Load()),
                                    Name(id='t', ctx=Load()),
                                    Name(id='format', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='t', ctx=Load()),
                                    attr='seek',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=0, kind=None)],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='base64', ctx=Load()),
                                            attr='b64encode',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='t', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='decode',
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
            decorator_list=[Name(id='check_db_management_enabled', ctx=Load())],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='dump_db_manifest',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='cr', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='pg_version', ctx=Store())],
                    value=BinOp(
                        left=Constant(value='%d.%d', kind=None),
                        op=Mod(),
                        right=Call(
                            func=Name(id='divmod', ctx=Load()),
                            args=[
                                BinOp(
                                    left=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='cr', ctx=Load()),
                                                attr='_obj',
                                                ctx=Load(),
                                            ),
                                            attr='connection',
                                            ctx=Load(),
                                        ),
                                        attr='server_version',
                                        ctx=Load(),
                                    ),
                                    op=Div(),
                                    right=Constant(value=100, kind=None),
                                ),
                                Constant(value=100, kind=None),
                            ],
                            keywords=[],
                        ),
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='cr', ctx=Load()),
                            attr='execute',
                            ctx=Load(),
                        ),
                        args=[Constant(value="SELECT name, latest_version FROM ir_module_module WHERE state = 'installed'", kind=None)],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='modules', ctx=Store())],
                    value=Call(
                        func=Name(id='dict', ctx=Load()),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='fetchall',
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
                Assign(
                    targets=[Name(id='manifest', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='odoo_dump', kind=None),
                            Constant(value='db_name', kind=None),
                            Constant(value='version', kind=None),
                            Constant(value='version_info', kind=None),
                            Constant(value='major_version', kind=None),
                            Constant(value='pg_version', kind=None),
                            Constant(value='modules', kind=None),
                        ],
                        values=[
                            Constant(value='1', kind=None),
                            Attribute(
                                value=Name(id='cr', ctx=Load()),
                                attr='dbname',
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='release',
                                    ctx=Load(),
                                ),
                                attr='version',
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='release',
                                    ctx=Load(),
                                ),
                                attr='version_info',
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='release',
                                    ctx=Load(),
                                ),
                                attr='major_version',
                                ctx=Load(),
                            ),
                            Name(id='pg_version', ctx=Load()),
                            Name(id='modules', ctx=Load()),
                        ],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Name(id='manifest', ctx=Load()),
                ),
            ],
            decorator_list=[Name(id='check_db_management_enabled', ctx=Load())],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='dump_db',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='db_name', annotation=None, type_comment=None),
                    arg(arg='stream', annotation=None, type_comment=None),
                    arg(arg='backup_format', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value='zip', kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value='Dump database `db` into file-like object `stream` if stream is None\n    return a file object with the dump ', kind=None),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='_logger', ctx=Load()),
                            attr='info',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='DUMP DB: %s format %s', kind=None),
                            Name(id='db_name', ctx=Load()),
                            Name(id='backup_format', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='cmd', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='pg_dump', kind=None),
                            Constant(value='--no-owner', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='cmd', ctx=Load()),
                            attr='append',
                            ctx=Load(),
                        ),
                        args=[Name(id='db_name', ctx=Load())],
                        keywords=[],
                    ),
                ),
                If(
                    test=Compare(
                        left=Name(id='backup_format', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Constant(value='zip', kind=None)],
                    ),
                    body=[
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='tempfile', ctx=Load()),
                                            attr='TemporaryDirectory',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='dump_dir', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='filestore', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='odoo', ctx=Load()),
                                                    attr='tools',
                                                    ctx=Load(),
                                                ),
                                                attr='config',
                                                ctx=Load(),
                                            ),
                                            attr='filestore',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='db_name', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='exists',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='filestore', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='shutil', ctx=Load()),
                                                    attr='copytree',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='filestore', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='os', ctx=Load()),
                                                                attr='path',
                                                                ctx=Load(),
                                                            ),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='dump_dir', ctx=Load()),
                                                            Constant(value='filestore', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='open', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='os', ctx=Load()),
                                                                attr='path',
                                                                ctx=Load(),
                                                            ),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='dump_dir', ctx=Load()),
                                                            Constant(value='manifest.json', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='w', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='fh', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[Name(id='db', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='odoo', ctx=Load()),
                                                        attr='sql_db',
                                                        ctx=Load(),
                                                    ),
                                                    attr='db_connect',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='db_name', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Attribute(
                                                            value=Name(id='db', ctx=Load()),
                                                            attr='cursor',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    optional_vars=Name(id='cr', ctx=Store()),
                                                ),
                                            ],
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='json', ctx=Load()),
                                                            attr='dump',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='dump_db_manifest', ctx=Load()),
                                                                args=[Name(id='cr', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Name(id='fh', ctx=Load()),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='indent',
                                                                value=Constant(value=4, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cmd', ctx=Load()),
                                            attr='insert',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                            BinOp(
                                                left=Constant(value='--file=', kind=None),
                                                op=Add(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='path',
                                                            ctx=Load(),
                                                        ),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Name(id='dump_dir', ctx=Load()),
                                                        Constant(value='dump.sql', kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='tools',
                                                ctx=Load(),
                                            ),
                                            attr='exec_pg_command',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Starred(
                                                value=Name(id='cmd', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Name(id='stream', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='odoo', ctx=Load()),
                                                            attr='tools',
                                                            ctx=Load(),
                                                        ),
                                                        attr='osutil',
                                                        ctx=Load(),
                                                    ),
                                                    attr='zip_dir',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='dump_dir', ctx=Load()),
                                                    Name(id='stream', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='include_dir',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='fnct_sort',
                                                        value=Lambda(
                                                            args=arguments(
                                                                posonlyargs=[],
                                                                args=[arg(arg='file_name', annotation=None, type_comment=None)],
                                                                vararg=None,
                                                                kwonlyargs=[],
                                                                kw_defaults=[],
                                                                kwarg=None,
                                                                defaults=[],
                                                            ),
                                                            body=Compare(
                                                                left=Name(id='file_name', ctx=Load()),
                                                                ops=[NotEq()],
                                                                comparators=[Constant(value='dump.sql', kind=None)],
                                                            ),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='t', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='tempfile', ctx=Load()),
                                                    attr='TemporaryFile',
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
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='odoo', ctx=Load()),
                                                            attr='tools',
                                                            ctx=Load(),
                                                        ),
                                                        attr='osutil',
                                                        ctx=Load(),
                                                    ),
                                                    attr='zip_dir',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='dump_dir', ctx=Load()),
                                                    Name(id='t', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='include_dir',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='fnct_sort',
                                                        value=Lambda(
                                                            args=arguments(
                                                                posonlyargs=[],
                                                                args=[arg(arg='file_name', annotation=None, type_comment=None)],
                                                                vararg=None,
                                                                kwonlyargs=[],
                                                                kw_defaults=[],
                                                                kwarg=None,
                                                                defaults=[],
                                                            ),
                                                            body=Compare(
                                                                left=Name(id='file_name', ctx=Load()),
                                                                ops=[NotEq()],
                                                                comparators=[Constant(value='dump.sql', kind=None)],
                                                            ),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='t', ctx=Load()),
                                                    attr='seek',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=0, kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        Return(
                                            value=Name(id='t', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cmd', ctx=Load()),
                                    attr='insert',
                                    ctx=Load(),
                                ),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                    Constant(value='--format=c', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='stdin', ctx=Store()),
                                        Name(id='stdout', ctx=Store()),
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
                                    attr='exec_pg_command_pipe',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Name(id='cmd', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='stream', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='shutil', ctx=Load()),
                                            attr='copyfileobj',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='stdout', ctx=Load()),
                                            Name(id='stream', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Name(id='stdout', ctx=Load()),
                                ),
                            ],
                        ),
                    ],
                ),
            ],
            decorator_list=[Name(id='check_db_management_enabled', ctx=Load())],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='exp_restore',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='db_name', annotation=None, type_comment=None),
                    arg(arg='data', annotation=None, type_comment=None),
                    arg(arg='copy', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=False, kind=None)],
            ),
            body=[
                FunctionDef(
                    name='chunks',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='d', annotation=None, type_comment=None),
                            arg(arg='n', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=8192, kind=None)],
                    ),
                    body=[
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    Constant(value=0, kind=None),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='d', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='n', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Yield(
                                        value=Subscript(
                                            value=Name(id='d', ctx=Load()),
                                            slice=Slice(
                                                lower=Name(id='i', ctx=Load()),
                                                upper=BinOp(
                                                    left=Name(id='i', ctx=Load()),
                                                    op=Add(),
                                                    right=Name(id='n', ctx=Load()),
                                                ),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='data_file', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='tempfile', ctx=Load()),
                            attr='NamedTemporaryFile',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='delete',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Try(
                    body=[
                        For(
                            target=Name(id='chunk', ctx=Store()),
                            iter=Call(
                                func=Name(id='chunks', ctx=Load()),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='data_file', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='base64', ctx=Load()),
                                                    attr='b64decode',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='chunk', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data_file', ctx=Load()),
                                    attr='close',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='restore_db', ctx=Load()),
                                args=[
                                    Name(id='db_name', ctx=Load()),
                                    Attribute(
                                        value=Name(id='data_file', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='copy',
                                        value=Name(id='copy', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    handlers=[],
                    orelse=[],
                    finalbody=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='data_file', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                ),
                Return(
                    value=Constant(value=True, kind=None),
                ),
            ],
            decorator_list=[Name(id='check_db_management_enabled', ctx=Load())],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='restore_db',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='db', annotation=None, type_comment=None),
                    arg(arg='dump_file', annotation=None, type_comment=None),
                    arg(arg='copy', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=False, kind=None)],
            ),
            body=[
                Assert(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='db', ctx=Load()),
                            Name(id='str', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    msg=None,
                ),
                If(
                    test=Call(
                        func=Name(id='exp_db_exist', ctx=Load()),
                        args=[Name(id='db', ctx=Load())],
                        keywords=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='RESTORE DB: %s already exists', kind=None),
                                    Name(id='db', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Raise(
                            exc=Call(
                                func=Name(id='Exception', ctx=Load()),
                                args=[Constant(value='Database already exists', kind=None)],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Expr(
                    value=Call(
                        func=Name(id='_create_empty_database', ctx=Load()),
                        args=[Name(id='db', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='filestore_path', ctx=Store())],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
                With(
                    items=[
                        withitem(
                            context_expr=Call(
                                func=Attribute(
                                    value=Name(id='tempfile', ctx=Load()),
                                    attr='TemporaryDirectory',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            optional_vars=Name(id='dump_dir', ctx=Store()),
                        ),
                    ],
                    body=[
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='zipfile', ctx=Load()),
                                    attr='is_zipfile',
                                    ctx=Load(),
                                ),
                                args=[Name(id='dump_file', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='zipfile', ctx=Load()),
                                                    attr='ZipFile',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='dump_file', ctx=Load()),
                                                    Constant(value='r', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='z', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[Name(id='filestore', ctx=Store())],
                                            value=ListComp(
                                                elt=Name(id='m', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='m', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='z', ctx=Load()),
                                                                attr='namelist',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ifs=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='m', ctx=Load()),
                                                                    attr='startswith',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='filestore/', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='z', ctx=Load()),
                                                    attr='extractall',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='dump_dir', ctx=Load()),
                                                    BinOp(
                                                        left=List(
                                                            elts=[Constant(value='dump.sql', kind=None)],
                                                            ctx=Load(),
                                                        ),
                                                        op=Add(),
                                                        right=Name(id='filestore', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=Name(id='filestore', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='filestore_path', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='os', ctx=Load()),
                                                                attr='path',
                                                                ctx=Load(),
                                                            ),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='dump_dir', ctx=Load()),
                                                            Constant(value='filestore', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='pg_cmd', ctx=Store())],
                                    value=Constant(value='psql', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='pg_args', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Constant(value='-q', kind=None),
                                            Constant(value='-f', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='dump_dir', ctx=Load()),
                                                    Constant(value='dump.sql', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='pg_cmd', ctx=Store())],
                                    value=Constant(value='pg_restore', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='pg_args', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Constant(value='--no-owner', kind=None),
                                            Name(id='dump_file', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='args', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='args', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='--dbname=', kind=None),
                                        op=Add(),
                                        right=Name(id='db', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='pg_args', ctx=Store())],
                            value=BinOp(
                                left=Name(id='args', ctx=Load()),
                                op=Add(),
                                right=Name(id='pg_args', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='tools',
                                        ctx=Load(),
                                    ),
                                    attr='exec_pg_command',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='pg_cmd', ctx=Load()),
                                    Starred(
                                        value=Name(id='pg_args', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='Exception', ctx=Load()),
                                        args=[Constant(value="Couldn't restore database", kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='registry', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='modules',
                                                ctx=Load(),
                                            ),
                                            attr='registry',
                                            ctx=Load(),
                                        ),
                                        attr='Registry',
                                        ctx=Load(),
                                    ),
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[Name(id='db', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='registry', ctx=Load()),
                                            attr='cursor',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='cr', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='env', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='api',
                                                ctx=Load(),
                                            ),
                                            attr='Environment',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='cr', ctx=Load()),
                                            Name(id='SUPERUSER_ID', ctx=Load()),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='copy', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='env', ctx=Load()),
                                                        slice=Constant(value='ir.config_parameter', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='init',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='force',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Name(id='filestore_path', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='filestore_dest', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='env', ctx=Load()),
                                                        slice=Constant(value='ir.attachment', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_filestore',
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
                                                    value=Name(id='shutil', ctx=Load()),
                                                    attr='move',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='filestore_path', ctx=Load()),
                                                    Name(id='filestore_dest', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='_logger', ctx=Load()),
                            attr='info',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='RESTORE DB: %s', kind=None),
                            Name(id='db', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[Name(id='check_db_management_enabled', ctx=Load())],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='exp_rename',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='old_name', annotation=None, type_comment=None),
                    arg(arg='new_name', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='modules',
                                        ctx=Load(),
                                    ),
                                    attr='registry',
                                    ctx=Load(),
                                ),
                                attr='Registry',
                                ctx=Load(),
                            ),
                            attr='delete',
                            ctx=Load(),
                        ),
                        args=[Name(id='old_name', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='sql_db',
                                ctx=Load(),
                            ),
                            attr='close_db',
                            ctx=Load(),
                        ),
                        args=[Name(id='old_name', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='db', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='sql_db',
                                ctx=Load(),
                            ),
                            attr='db_connect',
                            ctx=Load(),
                        ),
                        args=[Constant(value='postgres', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                With(
                    items=[
                        withitem(
                            context_expr=Call(
                                func=Name(id='closing', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='db', ctx=Load()),
                                            attr='cursor',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            optional_vars=Name(id='cr', ctx=Store()),
                        ),
                    ],
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='cr', ctx=Load()),
                                        attr='_cnx',
                                        ctx=Load(),
                                    ),
                                    attr='autocommit',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='_drop_conn', ctx=Load()),
                                args=[
                                    Name(id='cr', ctx=Load()),
                                    Name(id='old_name', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='sql', ctx=Load()),
                                                            attr='SQL',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='ALTER DATABASE {} RENAME TO {}', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='format',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='sql', ctx=Load()),
                                                            attr='Identifier',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='old_name', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='sql', ctx=Load()),
                                                            attr='Identifier',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='new_name', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='RENAME DB: %s -> %s', kind=None),
                                            Name(id='old_name', ctx=Load()),
                                            Name(id='new_name', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='e',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='info',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='RENAME DB: %s -> %s failed:\n%s', kind=None),
                                                    Name(id='old_name', ctx=Load()),
                                                    Name(id='new_name', ctx=Load()),
                                                    Name(id='e', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Raise(
                                            exc=Call(
                                                func=Name(id='Exception', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value="Couldn't rename database %s to %s: %s", kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='old_name', ctx=Load()),
                                                                Name(id='new_name', ctx=Load()),
                                                                Name(id='e', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='old_fs', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='tools',
                                    ctx=Load(),
                                ),
                                attr='config',
                                ctx=Load(),
                            ),
                            attr='filestore',
                            ctx=Load(),
                        ),
                        args=[Name(id='old_name', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='new_fs', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='tools',
                                    ctx=Load(),
                                ),
                                attr='config',
                                ctx=Load(),
                            ),
                            attr='filestore',
                            ctx=Load(),
                        ),
                        args=[Name(id='new_name', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='exists',
                                    ctx=Load(),
                                ),
                                args=[Name(id='old_fs', ctx=Load())],
                                keywords=[],
                            ),
                            UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='path',
                                            ctx=Load(),
                                        ),
                                        attr='exists',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='new_fs', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='shutil', ctx=Load()),
                                    attr='move',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='old_fs', ctx=Load()),
                                    Name(id='new_fs', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Constant(value=True, kind=None),
                ),
            ],
            decorator_list=[Name(id='check_db_management_enabled', ctx=Load())],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='exp_change_admin_password',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='new_password', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='tools',
                                    ctx=Load(),
                                ),
                                attr='config',
                                ctx=Load(),
                            ),
                            attr='set_admin_password',
                            ctx=Load(),
                        ),
                        args=[Name(id='new_password', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='tools',
                                    ctx=Load(),
                                ),
                                attr='config',
                                ctx=Load(),
                            ),
                            attr='save',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Constant(value=True, kind=None),
                ),
            ],
            decorator_list=[Name(id='check_db_management_enabled', ctx=Load())],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='exp_migrate_databases',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='databases', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                For(
                    target=Name(id='db', ctx=Store()),
                    iter=Name(id='databases', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='migrate database %s', kind=None),
                                    Name(id='db', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='tools',
                                                ctx=Load(),
                                            ),
                                            attr='config',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='update', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='base', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='modules',
                                                ctx=Load(),
                                            ),
                                            attr='registry',
                                            ctx=Load(),
                                        ),
                                        attr='Registry',
                                        ctx=Load(),
                                    ),
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[Name(id='db', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='force_demo',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='update_module',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Constant(value=True, kind=None),
                ),
            ],
            decorator_list=[Name(id='check_db_management_enabled', ctx=Load())],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='exp_db_exist',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='db_name', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Try(
                    body=[
                        Assign(
                            targets=[Name(id='db', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='sql_db',
                                        ctx=Load(),
                                    ),
                                    attr='db_connect',
                                    ctx=Load(),
                                ),
                                args=[Name(id='db_name', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='db', ctx=Load()),
                                            attr='cursor',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='Exception', ctx=Load()),
                            name=None,
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
            ],
            decorator_list=[
                Call(
                    func=Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='tools',
                            ctx=Load(),
                        ),
                        attr='mute_logger',
                        ctx=Load(),
                    ),
                    args=[Constant(value='odoo.sql_db', kind=None)],
                    keywords=[],
                ),
            ],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='list_dbs',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='force', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=False, kind=None)],
            ),
            body=[
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            UnaryOp(
                                op=Not(),
                                operand=Subscript(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='tools',
                                            ctx=Load(),
                                        ),
                                        attr='config',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='list_db', kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            UnaryOp(
                                op=Not(),
                                operand=Name(id='force', ctx=Load()),
                            ),
                        ],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='exceptions',
                                        ctx=Load(),
                                    ),
                                    attr='AccessDenied',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            UnaryOp(
                                op=Not(),
                                operand=Subscript(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='tools',
                                            ctx=Load(),
                                        ),
                                        attr='config',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='dbfilter', kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='tools',
                                        ctx=Load(),
                                    ),
                                    attr='config',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='db_name', kind=None),
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Name(id='sorted', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Name(id='db', ctx=Load()),
                                                attr='strip',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='db', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='odoo', ctx=Load()),
                                                                    attr='tools',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='config',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='db_name', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value=',', kind=None)],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='chosen_template', ctx=Store())],
                    value=Subscript(
                        value=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='tools',
                                ctx=Load(),
                            ),
                            attr='config',
                            ctx=Load(),
                        ),
                        slice=Constant(value='db_template', kind=None),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='templates_list', ctx=Store())],
                    value=Call(
                        func=Name(id='tuple', ctx=Load()),
                        args=[
                            Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='postgres', kind=None),
                                            Name(id='chosen_template', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='db', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='sql_db',
                                ctx=Load(),
                            ),
                            attr='db_connect',
                            ctx=Load(),
                        ),
                        args=[Constant(value='postgres', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                With(
                    items=[
                        withitem(
                            context_expr=Call(
                                func=Name(id='closing', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='db', ctx=Load()),
                                            attr='cursor',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            optional_vars=Name(id='cr', ctx=Store()),
                        ),
                    ],
                    body=[
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='select datname from pg_database where datdba=(select usesysid from pg_user where usename=current_user) and not datistemplate and datallowconn and datname not in %s order by datname', kind=None),
                                            Tuple(
                                                elts=[Name(id='templates_list', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=ListComp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='odoo', ctx=Load()),
                                                    attr='tools',
                                                    ctx=Load(),
                                                ),
                                                attr='ustr',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='name', ctx=Load())],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[Name(id='name', ctx=Store())],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='cr', ctx=Load()),
                                                        attr='fetchall',
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
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='exception',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='Listing databases failed:', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='res', ctx=Store())],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    type_comment=None,
                ),
                Return(
                    value=Name(id='res', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='list_db_incompatible',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='databases', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='"Check a list of databases if they are compatible with this version of Odoo\n\n        :param databases: A list of existing Postgresql databases\n        :return: A list of databases that are incompatible\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='incompatible_databases', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='server_version', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Constant(value='.', kind=None),
                            attr='join',
                            ctx=Load(),
                        ),
                        args=[
                            GeneratorExp(
                                elt=Call(
                                    func=Name(id='str', ctx=Load()),
                                    args=[Name(id='v', ctx=Load())],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='v', ctx=Store()),
                                        iter=Subscript(
                                            value=Name(id='version_info', ctx=Load()),
                                            slice=Slice(
                                                lower=None,
                                                upper=Constant(value=2, kind=None),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='database_name', ctx=Store()),
                    iter=Name(id='databases', ctx=Load()),
                    body=[
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='closing', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Name(id='db_connect', ctx=Load()),
                                                        args=[Name(id='database_name', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='cursor',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='cr', ctx=Store()),
                                ),
                            ],
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='tools',
                                                ctx=Load(),
                                            ),
                                            attr='table_exists',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='cr', ctx=Load()),
                                            Constant(value='ir_module_module', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='cr', ctx=Load()),
                                                    attr='execute',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='SELECT latest_version FROM ir_module_module WHERE name=%s', kind=None),
                                                    Tuple(
                                                        elts=[Constant(value='base', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='base_version', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='cr', ctx=Load()),
                                                    attr='fetchone',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='base_version', ctx=Load()),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Subscript(
                                                            value=Name(id='base_version', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='incompatible_databases', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='database_name', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='local_version', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Constant(value='.', kind=None),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='base_version', ctx=Load()),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='split',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='.', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                slice=Slice(
                                                                    lower=None,
                                                                    upper=Constant(value=2, kind=None),
                                                                    step=None,
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='local_version', ctx=Load()),
                                                        ops=[NotEq()],
                                                        comparators=[Name(id='server_version', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='incompatible_databases', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='database_name', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='incompatible_databases', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='database_name', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                For(
                    target=Name(id='database_name', ctx=Store()),
                    iter=Name(id='incompatible_databases', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='sql_db',
                                        ctx=Load(),
                                    ),
                                    attr='close_db',
                                    ctx=Load(),
                                ),
                                args=[Name(id='database_name', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Name(id='incompatible_databases', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='exp_list',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='document', annotation=None, type_comment=None)],
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
                        operand=Subscript(
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='tools',
                                    ctx=Load(),
                                ),
                                attr='config',
                                ctx=Load(),
                            ),
                            slice=Constant(value='list_db', kind=None),
                            ctx=Load(),
                        ),
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='exceptions',
                                        ctx=Load(),
                                    ),
                                    attr='AccessDenied',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Name(id='list_dbs', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='exp_list_lang',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Return(
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='tools',
                                ctx=Load(),
                            ),
                            attr='scan_languages',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='exp_list_countries',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Assign(
                    targets=[Name(id='list_countries', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='root', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ET', ctx=Load()),
                                    attr='parse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='odoo', ctx=Load()),
                                                        attr='tools',
                                                        ctx=Load(),
                                                    ),
                                                    attr='config',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='root_path', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value='addons/base/data/res_country_data.xml', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            attr='getroot',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='country', ctx=Store()),
                    iter=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='root', ctx=Load()),
                                    attr='find',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='data', kind=None)],
                                keywords=[],
                            ),
                            attr='findall',
                            ctx=Load(),
                        ),
                        args=[Constant(value='record[@model="res.country"]', kind=None)],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='name', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='country', ctx=Load()),
                                        attr='find',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='field[@name="name"]', kind=None)],
                                    keywords=[],
                                ),
                                attr='text',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='code', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='country', ctx=Load()),
                                        attr='find',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='field[@name="code"]', kind=None)],
                                    keywords=[],
                                ),
                                attr='text',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='list_countries', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Name(id='code', ctx=Load()),
                                            Name(id='name', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Name(id='sorted', ctx=Load()),
                        args=[Name(id='list_countries', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='key',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='c', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Subscript(
                                        value=Name(id='c', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                ),
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
            name='exp_server_version',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Expr(
                    value=Constant(value=' Return the version of the server\n        Used by the client to verify the compatibility with its own version\n    ', kind=None),
                ),
                Return(
                    value=Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='release',
                            ctx=Load(),
                        ),
                        attr='version',
                        ctx=Load(),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='dispatch',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='method', annotation=None, type_comment=None),
                    arg(arg='params', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='g', ctx=Store())],
                    value=Call(
                        func=Name(id='globals', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='exp_method_name', ctx=Store())],
                    value=BinOp(
                        left=Constant(value='exp_', kind=None),
                        op=Add(),
                        right=Name(id='method', ctx=Load()),
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='method', ctx=Load()),
                        ops=[In()],
                        comparators=[
                            List(
                                elts=[
                                    Constant(value='db_exist', kind=None),
                                    Constant(value='list', kind=None),
                                    Constant(value='list_lang', kind=None),
                                    Constant(value='server_version', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Subscript(
                                    value=Name(id='g', ctx=Load()),
                                    slice=Name(id='exp_method_name', ctx=Load()),
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Name(id='params', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[
                        If(
                            test=Compare(
                                left=Name(id='exp_method_name', ctx=Load()),
                                ops=[In()],
                                comparators=[Name(id='g', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='passwd', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='params', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='params', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='params', ctx=Load()),
                                        slice=Slice(
                                            lower=Constant(value=1, kind=None),
                                            upper=None,
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='check_super', ctx=Load()),
                                        args=[Name(id='passwd', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Call(
                                        func=Subscript(
                                            value=Name(id='g', ctx=Load()),
                                            slice=Name(id='exp_method_name', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Starred(
                                                value=Name(id='params', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='KeyError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='Method not found: %s', kind=None),
                                                op=Mod(),
                                                right=Name(id='method', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                        ),
                    ],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
