Module(
    body=[
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        ImportFrom(
            module='importlib',
            names=[alias(name='util', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='io', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='netifaces', asname=None)],
        ),
        ImportFrom(
            module='OpenSSL',
            names=[alias(name='crypto', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        ImportFrom(
            module='pathlib',
            names=[alias(name='Path', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='subprocess', asname=None)],
        ),
        Import(
            names=[alias(name='urllib3', asname=None)],
        ),
        Import(
            names=[alias(name='zipfile', asname=None)],
        ),
        ImportFrom(
            module='threading',
            names=[alias(name='Thread', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='http', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.modules.module',
            names=[alias(name='get_resource_path', asname=None)],
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
            name='IoTRestart',
            bases=[Name(id='Thread', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n    Thread to restart odoo server in IoT Box when we must return a answer before\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='delay', annotation=None, type_comment=None),
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
                                    value=Name(id='Thread', ctx=Load()),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='delay',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='delay', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='run',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='time', ctx=Load()),
                                    attr='sleep',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='delay',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='check_call',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='sudo', kind=None),
                                            Constant(value='service', kind=None),
                                            Constant(value='odoo', kind=None),
                                            Constant(value='restart', kind=None),
                                        ],
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
            ],
            decorator_list=[],
        ),
        FunctionDef(
            name='access_point',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Return(
                    value=Compare(
                        left=Call(
                            func=Name(id='get_ip', ctx=Load()),
                            args=[],
                            keywords=[],
                        ),
                        ops=[Eq()],
                        comparators=[Constant(value='10.11.12.1', kind=None)],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='add_credential',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='db_uuid', annotation=None, type_comment=None),
                    arg(arg='enterprise_code', annotation=None, type_comment=None),
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
                        func=Name(id='write_file', ctx=Load()),
                        args=[
                            Constant(value='odoo-db-uuid.conf', kind=None),
                            Name(id='db_uuid', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Name(id='write_file', ctx=Load()),
                        args=[
                            Constant(value='odoo-enterprise-code.conf', kind=None),
                            Name(id='enterprise_code', ctx=Load()),
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
            name='check_certificate',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Expr(
                    value=Constant(value='\n    Check if the current certificate is up to date or not authenticated\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='server', ctx=Store())],
                    value=Call(
                        func=Name(id='get_odoo_server_url', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='server', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='path', ctx=Store())],
                            value=Call(
                                func=Name(id='Path', ctx=Load()),
                                args=[Constant(value='/etc/ssl/certs/nginx-cert.crt', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='path', ctx=Load()),
                                    attr='exists',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='path', ctx=Load()),
                                                    attr='open',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='r', kind=None)],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='f', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[Name(id='cert', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='crypto', ctx=Load()),
                                                    attr='load_certificate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='crypto', ctx=Load()),
                                                        attr='FILETYPE_PEM',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='f', ctx=Load()),
                                                            attr='read',
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
                                            targets=[Name(id='cert_end_date', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='datetime', ctx=Load()),
                                                            attr='datetime',
                                                            ctx=Load(),
                                                        ),
                                                        attr='strptime',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='cert', ctx=Load()),
                                                                        attr='get_notAfter',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                attr='decode',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='utf-8', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        Constant(value='%Y%m%d%H%M%SZ', kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Sub(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Name(id='datetime', ctx=Load()),
                                                        attr='timedelta',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='days',
                                                            value=Constant(value=10, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='key', ctx=Store()),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='cert', ctx=Load()),
                                                            attr='get_subject',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='get_components',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Subscript(
                                                            value=Name(id='key', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value=b'CN', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='cn', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Name(id='key', ctx=Load()),
                                                                        slice=Constant(value=1, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='decode',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='utf-8', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='cn', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='OdooTempIoTBoxCertificate', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='datetime', ctx=Load()),
                                                                    attr='datetime',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='now',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ops=[Gt()],
                                                        comparators=[Name(id='cert_end_date', ctx=Load())],
                                                    ),
                                                ],
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
                                                            BinOp(
                                                                left=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value='Your certificate %s must be updated', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                op=Mod(),
                                                                right=Name(id='cn', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='load_certificate', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
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
                                                            BinOp(
                                                                left=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value='Your certificate %s is valid until %s', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Name(id='cn', ctx=Load()),
                                                                        Name(id='cert_end_date', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
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
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Name(id='load_certificate', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
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
            name='check_git_branch',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Expr(
                    value=Constant(value='\n    Check if the local branch is the same than the connected Odoo DB and\n    checkout to match it if needed.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='server', ctx=Store())],
                    value=Call(
                        func=Name(id='get_odoo_server_url', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='server', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='urllib3', ctx=Load()),
                                    attr='disable_warnings',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='http', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='urllib3', ctx=Load()),
                                    attr='PoolManager',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='cert_reqs',
                                        value=Constant(value='CERT_NONE', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='response', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='http', ctx=Load()),
                                            attr='request',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='POST', kind=None),
                                            BinOp(
                                                left=Name(id='server', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value='/web/webclient/version_info', kind=None),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='body',
                                                value=Constant(value='{}', kind=None),
                                            ),
                                            keyword(
                                                arg='headers',
                                                value=Dict(
                                                    keys=[Constant(value='Content-type', kind=None)],
                                                    values=[Constant(value='application/json', kind=None)],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='response', ctx=Load()),
                                            attr='status',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=200, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='git', ctx=Store())],
                                            value=List(
                                                elts=[
                                                    Constant(value='git', kind=None),
                                                    Constant(value='--work-tree=/home/pi/odoo/', kind=None),
                                                    Constant(value='--git-dir=/home/pi/odoo/.git', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='db_branch', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Subscript(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='json', ctx=Load()),
                                                                    attr='loads',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='response', ctx=Load()),
                                                                        attr='data',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            slice=Constant(value='result', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='server_serie', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='~', kind=None),
                                                    Constant(value='-', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='subprocess', ctx=Load()),
                                                        attr='check_output',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        BinOp(
                                                            left=Name(id='git', ctx=Load()),
                                                            op=Add(),
                                                            right=List(
                                                                elts=[
                                                                    Constant(value='ls-remote', kind=None),
                                                                    Constant(value='origin', kind=None),
                                                                    Name(id='db_branch', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='db_branch', ctx=Store())],
                                                    value=Constant(value='master', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='local_branch', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='subprocess', ctx=Load()),
                                                                    attr='check_output',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    BinOp(
                                                                        left=Name(id='git', ctx=Load()),
                                                                        op=Add(),
                                                                        right=List(
                                                                            elts=[
                                                                                Constant(value='symbolic-ref', kind=None),
                                                                                Constant(value='-q', kind=None),
                                                                                Constant(value='--short', kind=None),
                                                                                Constant(value='HEAD', kind=None),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='decode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='utf-8', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='rstrip',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='db_branch', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Name(id='local_branch', ctx=Load())],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='subprocess', ctx=Load()),
                                                            attr='call',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='sudo', kind=None),
                                                                    Constant(value='mount', kind=None),
                                                                    Constant(value='-o', kind=None),
                                                                    Constant(value='remount,rw', kind=None),
                                                                    Constant(value='/', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='subprocess', ctx=Load()),
                                                            attr='check_call',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='rm', kind=None),
                                                                    Constant(value='-rf', kind=None),
                                                                    Constant(value='/home/pi/odoo/addons/hw_drivers/iot_handlers/drivers/*', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='subprocess', ctx=Load()),
                                                            attr='check_call',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='rm', kind=None),
                                                                    Constant(value='-rf', kind=None),
                                                                    Constant(value='/home/pi/odoo/addons/hw_drivers/iot_handlers/interfaces/*', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='subprocess', ctx=Load()),
                                                            attr='check_call',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Name(id='git', ctx=Load()),
                                                                op=Add(),
                                                                right=List(
                                                                    elts=[
                                                                        Constant(value='branch', kind=None),
                                                                        Constant(value='-m', kind=None),
                                                                        Name(id='db_branch', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='subprocess', ctx=Load()),
                                                            attr='check_call',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Name(id='git', ctx=Load()),
                                                                op=Add(),
                                                                right=List(
                                                                    elts=[
                                                                        Constant(value='remote', kind=None),
                                                                        Constant(value='set-branches', kind=None),
                                                                        Constant(value='origin', kind=None),
                                                                        Name(id='db_branch', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='os', ctx=Load()),
                                                            attr='system',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='/home/pi/odoo/addons/point_of_sale/tools/posbox/configuration/posbox_update.sh', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='subprocess', ctx=Load()),
                                                            attr='call',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='sudo', kind=None),
                                                                    Constant(value='mount', kind=None),
                                                                    Constant(value='-o', kind=None),
                                                                    Constant(value='remount,ro', kind=None),
                                                                    Constant(value='/', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='subprocess', ctx=Load()),
                                                            attr='call',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='sudo', kind=None),
                                                                    Constant(value='mount', kind=None),
                                                                    Constant(value='-o', kind=None),
                                                                    Constant(value='remount,rw', kind=None),
                                                                    Constant(value='/root_bypass_ramdisks/etc/cups', kind=None),
                                                                ],
                                                                ctx=Load(),
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
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='Could not reach configured server', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='A error encountered : %s ', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='e', ctx=Load()),
                                                    ),
                                                ],
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
                    orelse=[],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='check_image',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Expr(
                    value=Constant(value='\n    Check if the current image of IoT Box is up to date\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='url', ctx=Store())],
                    value=Constant(value='https://nightly.odoo.com/master/iotbox/SHA1SUMS.txt', kind=None),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='urllib3', ctx=Load()),
                            attr='disable_warnings',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='http', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='urllib3', ctx=Load()),
                            attr='PoolManager',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='cert_reqs',
                                value=Constant(value='CERT_NONE', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='response', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='http', ctx=Load()),
                            attr='request',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='GET', kind=None),
                            Name(id='url', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='checkFile', ctx=Store())],
                    value=Dict(keys=[], values=[]),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='valueActual', ctx=Store())],
                    value=Constant(value='', kind=None),
                    type_comment=None,
                ),
                For(
                    target=Name(id='line', ctx=Store()),
                    iter=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='response', ctx=Load()),
                                        attr='data',
                                        ctx=Load(),
                                    ),
                                    attr='decode',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            attr='split',
                            ctx=Load(),
                        ),
                        args=[Constant(value='\n', kind=None)],
                        keywords=[],
                    ),
                    body=[
                        If(
                            test=Name(id='line', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='value', ctx=Store()),
                                                Name(id='name', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='  ', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='checkFile', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Name(id='value', ctx=Load())],
                                                values=[Name(id='name', ctx=Load())],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='name', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='iotbox-latest.zip', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='valueLastest', ctx=Store())],
                                            value=Name(id='value', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='name', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[
                                                    Call(
                                                        func=Name(id='get_img_name', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='valueActual', ctx=Store())],
                                                    value=Name(id='value', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='valueActual', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Name(id='valueLastest', ctx=Load())],
                    ),
                    body=[
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='version', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='checkFile', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='valueLastest', ctx=Load()),
                                                    Constant(value='Error', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='iotboxv', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='.zip', kind=None),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                            attr='split',
                            ctx=Load(),
                        ),
                        args=[Constant(value='_', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Dict(
                        keys=[
                            Constant(value='major', kind=None),
                            Constant(value='minor', kind=None),
                        ],
                        values=[
                            Subscript(
                                value=Name(id='version', ctx=Load()),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            Subscript(
                                value=Name(id='version', ctx=Load()),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
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
            name='get_img_name',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='major', ctx=Store()),
                                Name(id='minor', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Name(id='get_version', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            attr='split',
                            ctx=Load(),
                        ),
                        args=[Constant(value='.', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=BinOp(
                        left=Constant(value='iotboxv%s_%s.zip', kind=None),
                        op=Mod(),
                        right=Tuple(
                            elts=[
                                Name(id='major', ctx=Load()),
                                Name(id='minor', ctx=Load()),
                            ],
                            ctx=Load(),
                        ),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='get_ip',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                While(
                    test=Constant(value=True, kind=None),
                    body=[
                        Try(
                            body=[
                                Return(
                                    value=Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='netifaces', ctx=Load()),
                                                        attr='ifaddresses',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='eth0', kind=None)],
                                                    keywords=[],
                                                ),
                                                slice=Attribute(
                                                    value=Name(id='netifaces', ctx=Load()),
                                                    attr='AF_INET',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='addr', kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='KeyError', ctx=Load()),
                                    name=None,
                                    body=[Pass()],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Try(
                            body=[
                                Return(
                                    value=Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='netifaces', ctx=Load()),
                                                        attr='ifaddresses',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='wlan0', kind=None)],
                                                    keywords=[],
                                                ),
                                                slice=Attribute(
                                                    value=Name(id='netifaces', ctx=Load()),
                                                    attr='AF_INET',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='addr', kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='KeyError', ctx=Load()),
                                    name=None,
                                    body=[Pass()],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='warning',
                                    ctx=Load(),
                                ),
                                args=[Constant(value="Couldn't get IP, sleeping and retrying.", kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='time', ctx=Load()),
                                    attr='sleep',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=5, kind=None)],
                                keywords=[],
                            ),
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
            name='get_mac_address',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                While(
                    test=Constant(value=True, kind=None),
                    body=[
                        Try(
                            body=[
                                Return(
                                    value=Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='netifaces', ctx=Load()),
                                                        attr='ifaddresses',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='eth0', kind=None)],
                                                    keywords=[],
                                                ),
                                                slice=Attribute(
                                                    value=Name(id='netifaces', ctx=Load()),
                                                    attr='AF_LINK',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='addr', kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='KeyError', ctx=Load()),
                                    name=None,
                                    body=[Pass()],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Try(
                            body=[
                                Return(
                                    value=Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='netifaces', ctx=Load()),
                                                        attr='ifaddresses',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='wlan0', kind=None)],
                                                    keywords=[],
                                                ),
                                                slice=Attribute(
                                                    value=Name(id='netifaces', ctx=Load()),
                                                    attr='AF_LINK',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='addr', kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='KeyError', ctx=Load()),
                                    name=None,
                                    body=[Pass()],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='warning',
                                    ctx=Load(),
                                ),
                                args=[Constant(value="Couldn't get MAC address, sleeping and retrying.", kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='time', ctx=Load()),
                                    attr='sleep',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=5, kind=None)],
                                keywords=[],
                            ),
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
            name='get_ssid',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Assign(
                    targets=[Name(id='ap', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='subprocess', ctx=Load()),
                            attr='call',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Constant(value='systemctl', kind=None),
                                    Constant(value='is-active', kind=None),
                                    Constant(value='--quiet', kind=None),
                                    Constant(value='hostapd', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='ap', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='subprocess', ctx=Load()),
                                                    attr='check_output',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='grep', kind=None),
                                                            Constant(value='-oP', kind=None),
                                                            Constant(value='(?<=ssid=).*', kind=None),
                                                            Constant(value='/etc/hostapd/hostapd.conf', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='decode',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='utf-8', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='rstrip',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='process_iwconfig', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='subprocess', ctx=Load()),
                            attr='Popen',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[Constant(value='iwconfig', kind=None)],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='stdout',
                                value=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='PIPE',
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='stderr',
                                value=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='STDOUT',
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='process_grep', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='subprocess', ctx=Load()),
                            attr='Popen',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Constant(value='grep', kind=None),
                                    Constant(value='ESSID:"', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='stdin',
                                value=Attribute(
                                    value=Name(id='process_iwconfig', ctx=Load()),
                                    attr='stdout',
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='stdout',
                                value=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='PIPE',
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='subprocess', ctx=Load()),
                                            attr='check_output',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='sed', kind=None),
                                                    Constant(value='s/.*"\\(.*\\)"/\\1/', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='stdin',
                                                value=Attribute(
                                                    value=Name(id='process_grep', ctx=Load()),
                                                    attr='stdout',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    attr='decode',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='utf-8', kind=None)],
                                keywords=[],
                            ),
                            attr='rstrip',
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
            name='get_odoo_server_url',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Assign(
                    targets=[Name(id='ap', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='subprocess', ctx=Load()),
                            attr='call',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Constant(value='systemctl', kind=None),
                                    Constant(value='is-active', kind=None),
                                    Constant(value='--quiet', kind=None),
                                    Constant(value='hostapd', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='ap', ctx=Load()),
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
                        func=Name(id='read_file_first_line', ctx=Load()),
                        args=[Constant(value='odoo-remote-server.conf', kind=None)],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='get_token',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Return(
                    value=Call(
                        func=Name(id='read_file_first_line', ctx=Load()),
                        args=[Constant(value='token', kind=None)],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='get_version',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Return(
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='subprocess', ctx=Load()),
                                            attr='check_output',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='cat', kind=None),
                                                    Constant(value='/var/odoo/iotbox_version', kind=None),
                                                ],
                                                ctx=Load(),
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
                            attr='rstrip',
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
            name='get_wifi_essid',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Assign(
                    targets=[Name(id='wifi_options', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='process_iwlist', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='subprocess', ctx=Load()),
                            attr='Popen',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Constant(value='sudo', kind=None),
                                    Constant(value='iwlist', kind=None),
                                    Constant(value='wlan0', kind=None),
                                    Constant(value='scan', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='stdout',
                                value=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='PIPE',
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='stderr',
                                value=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='STDOUT',
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='process_grep', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='subprocess', ctx=Load()),
                                        attr='Popen',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Constant(value='grep', kind=None),
                                                Constant(value='ESSID:"', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='stdin',
                                            value=Attribute(
                                                value=Name(id='process_iwlist', ctx=Load()),
                                                attr='stdout',
                                                ctx=Load(),
                                            ),
                                        ),
                                        keyword(
                                            arg='stdout',
                                            value=Attribute(
                                                value=Name(id='subprocess', ctx=Load()),
                                                attr='PIPE',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                                attr='stdout',
                                ctx=Load(),
                            ),
                            attr='readlines',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='ssid', ctx=Store()),
                    iter=Name(id='process_grep', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='essid', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='ssid', ctx=Load()),
                                                attr='decode',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='utf-8', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='split',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='"', kind=None)],
                                    keywords=[],
                                ),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='essid', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[Name(id='wifi_options', ctx=Load())],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='wifi_options', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='essid', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Name(id='wifi_options', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='load_certificate',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Expr(
                    value=Constant(value='\n    Send a request to Odoo with customer db_uuid and enterprise_code to get a true certificate\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='db_uuid', ctx=Store())],
                    value=Call(
                        func=Name(id='read_file_first_line', ctx=Load()),
                        args=[Constant(value='odoo-db-uuid.conf', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='enterprise_code', ctx=Store())],
                    value=Call(
                        func=Name(id='read_file_first_line', ctx=Load()),
                        args=[Constant(value='odoo-enterprise-code.conf', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Name(id='db_uuid', ctx=Load()),
                            Name(id='enterprise_code', ctx=Load()),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=Constant(value='https://www.odoo.com/odoo-enterprise/iot/x509', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='params', kind=None)],
                                values=[
                                    Dict(
                                        keys=[
                                            Constant(value='db_uuid', kind=None),
                                            Constant(value='enterprise_code', kind=None),
                                        ],
                                        values=[
                                            Name(id='db_uuid', ctx=Load()),
                                            Name(id='enterprise_code', ctx=Load()),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='urllib3', ctx=Load()),
                                    attr='disable_warnings',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='http', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='urllib3', ctx=Load()),
                                    attr='PoolManager',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='cert_reqs',
                                        value=Constant(value='CERT_NONE', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='http', ctx=Load()),
                                    attr='request',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='POST', kind=None),
                                    Name(id='url', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='body',
                                        value=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='json', ctx=Load()),
                                                        attr='dumps',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='data', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                attr='encode',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='utf8', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='headers',
                                        value=Dict(
                                            keys=[
                                                Constant(value='Content-type', kind=None),
                                                Constant(value='Accept', kind=None),
                                            ],
                                            values=[
                                                Constant(value='application/json', kind=None),
                                                Constant(value='text/plain', kind=None),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='json', ctx=Load()),
                                        attr='loads',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='response', ctx=Load()),
                                                    attr='data',
                                                    ctx=Load(),
                                                ),
                                                attr='decode',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='utf8', kind=None)],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value='result', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='result', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='write_file', ctx=Load()),
                                        args=[
                                            Constant(value='odoo-subject.conf', kind=None),
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='subject_cn', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='subprocess', ctx=Load()),
                                            attr='call',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='sudo', kind=None),
                                                    Constant(value='mount', kind=None),
                                                    Constant(value='-o', kind=None),
                                                    Constant(value='remount,rw', kind=None),
                                                    Constant(value='/', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='subprocess', ctx=Load()),
                                            attr='call',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='sudo', kind=None),
                                                    Constant(value='mount', kind=None),
                                                    Constant(value='-o', kind=None),
                                                    Constant(value='remount,rw', kind=None),
                                                    Constant(value='/root_bypass_ramdisks/', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='Path', ctx=Load()),
                                                args=[Constant(value='/etc/ssl/certs/nginx-cert.crt', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='write_text',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='x509_pem', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='Path', ctx=Load()),
                                                args=[Constant(value='/root_bypass_ramdisks/etc/ssl/certs/nginx-cert.crt', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='write_text',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='x509_pem', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='Path', ctx=Load()),
                                                args=[Constant(value='/etc/ssl/private/nginx-cert.key', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='write_text',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='private_key_pem', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='Path', ctx=Load()),
                                                args=[Constant(value='/root_bypass_ramdisks/etc/ssl/private/nginx-cert.key', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='write_text',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='private_key_pem', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='subprocess', ctx=Load()),
                                            attr='call',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='sudo', kind=None),
                                                    Constant(value='mount', kind=None),
                                                    Constant(value='-o', kind=None),
                                                    Constant(value='remount,ro', kind=None),
                                                    Constant(value='/', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='subprocess', ctx=Load()),
                                            attr='call',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='sudo', kind=None),
                                                    Constant(value='mount', kind=None),
                                                    Constant(value='-o', kind=None),
                                                    Constant(value='remount,ro', kind=None),
                                                    Constant(value='/root_bypass_ramdisks/', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='subprocess', ctx=Load()),
                                            attr='call',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='sudo', kind=None),
                                                    Constant(value='mount', kind=None),
                                                    Constant(value='-o', kind=None),
                                                    Constant(value='remount,rw', kind=None),
                                                    Constant(value='/root_bypass_ramdisks/etc/cups', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='subprocess', ctx=Load()),
                                            attr='check_call',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='sudo', kind=None),
                                                    Constant(value='service', kind=None),
                                                    Constant(value='nginx', kind=None),
                                                    Constant(value='restart', kind=None),
                                                ],
                                                ctx=Load(),
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
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='download_iot_handlers',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='auto', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=True, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Get the drivers from the configured Odoo server\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='server', ctx=Store())],
                    value=Call(
                        func=Name(id='get_odoo_server_url', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='server', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='urllib3', ctx=Load()),
                                    attr='disable_warnings',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='pm', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='urllib3', ctx=Load()),
                                    attr='PoolManager',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='cert_reqs',
                                        value=Constant(value='CERT_NONE', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='server', ctx=Store())],
                            value=BinOp(
                                left=Name(id='server', ctx=Load()),
                                op=Add(),
                                right=Constant(value='/iot/get_handlers', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='resp', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='pm', ctx=Load()),
                                            attr='request',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='POST', kind=None),
                                            Name(id='server', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='fields',
                                                value=Dict(
                                                    keys=[
                                                        Constant(value='mac', kind=None),
                                                        Constant(value='auto', kind=None),
                                                    ],
                                                    values=[
                                                        Call(
                                                            func=Name(id='get_mac_address', ctx=Load()),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        Name(id='auto', ctx=Load()),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='resp', ctx=Load()),
                                        attr='data',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='subprocess', ctx=Load()),
                                                    attr='call',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='sudo', kind=None),
                                                            Constant(value='mount', kind=None),
                                                            Constant(value='-o', kind=None),
                                                            Constant(value='remount,rw', kind=None),
                                                            Constant(value='/', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='drivers_path', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='Path', ctx=Load()),
                                                        attr='home',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                op=Div(),
                                                right=Constant(value='odoo/addons/hw_drivers/iot_handlers', kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='zip_file', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='zipfile', ctx=Load()),
                                                    attr='ZipFile',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='io', ctx=Load()),
                                                            attr='BytesIO',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='resp', ctx=Load()),
                                                                attr='data',
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
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='zip_file', ctx=Load()),
                                                    attr='extractall',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='drivers_path', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='subprocess', ctx=Load()),
                                                    attr='call',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='sudo', kind=None),
                                                            Constant(value='mount', kind=None),
                                                            Constant(value='-o', kind=None),
                                                            Constant(value='remount,ro', kind=None),
                                                            Constant(value='/', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='subprocess', ctx=Load()),
                                                    attr='call',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='sudo', kind=None),
                                                            Constant(value='mount', kind=None),
                                                            Constant(value='-o', kind=None),
                                                            Constant(value='remount,rw', kind=None),
                                                            Constant(value='/root_bypass_ramdisks/etc/cups', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
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
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='Could not reach configured server', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='A error encountered : %s ', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='e', ctx=Load()),
                                                    ),
                                                ],
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
                    orelse=[],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='load_iot_handlers',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Expr(
                    value=Constant(value="\n    This method loads local files: 'odoo/addons/hw_drivers/iot_handlers/drivers' and\n    'odoo/addons/hw_drivers/iot_handlers/interfaces'\n    And execute these python drivers and interfaces\n    ", kind=None),
                ),
                For(
                    target=Name(id='directory', ctx=Store()),
                    iter=List(
                        elts=[
                            Constant(value='interfaces', kind=None),
                            Constant(value='drivers', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='path', ctx=Store())],
                            value=Call(
                                func=Name(id='get_resource_path', ctx=Load()),
                                args=[
                                    Constant(value='hw_drivers', kind=None),
                                    Constant(value='iot_handlers', kind=None),
                                    Name(id='directory', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='filesList', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='listdir',
                                    ctx=Load(),
                                ),
                                args=[Name(id='path', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='file', ctx=Store()),
                            iter=Name(id='filesList', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='path_file', ctx=Store())],
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
                                            Name(id='path', ctx=Load()),
                                            Name(id='file', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='spec', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='util', ctx=Load()),
                                            attr='spec_from_file_location',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='file', ctx=Load()),
                                            Name(id='path_file', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='spec', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='module', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='util', ctx=Load()),
                                                    attr='module_from_spec',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='spec', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='spec', ctx=Load()),
                                                        attr='loader',
                                                        ctx=Load(),
                                                    ),
                                                    attr='exec_module',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='module', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Assign(
                    targets=[
                        Attribute(
                            value=Name(id='http', ctx=Load()),
                            attr='addons_manifest',
                            ctx=Store(),
                        ),
                    ],
                    value=Dict(keys=[], values=[]),
                    type_comment=None,
                ),
                Assign(
                    targets=[
                        Attribute(
                            value=Name(id='http', ctx=Load()),
                            attr='root',
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        func=Attribute(
                            value=Name(id='http', ctx=Load()),
                            attr='Root',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='odoo_restart',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='delay', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='IR', ctx=Store())],
                    value=Call(
                        func=Name(id='IoTRestart', ctx=Load()),
                        args=[Name(id='delay', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='IR', ctx=Load()),
                            attr='start',
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
            name='read_file_first_line',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='filename', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='path', ctx=Store())],
                    value=BinOp(
                        left=Call(
                            func=Attribute(
                                value=Name(id='Path', ctx=Load()),
                                attr='home',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                        op=Div(),
                        right=Name(id='filename', ctx=Load()),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='path', ctx=Store())],
                    value=Call(
                        func=Name(id='Path', ctx=Load()),
                        args=[
                            BinOp(
                                left=Constant(value='/home/pi/', kind=None),
                                op=Add(),
                                right=Name(id='filename', ctx=Load()),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Call(
                        func=Attribute(
                            value=Name(id='path', ctx=Load()),
                            attr='exists',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    body=[
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='path', ctx=Load()),
                                            attr='open',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='r', kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='f', ctx=Store()),
                                ),
                            ],
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='f', ctx=Load()),
                                                    attr='readline',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='\n', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Constant(value='', kind=None),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='unlink_file',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='filename', annotation=None, type_comment=None)],
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
                            value=Name(id='subprocess', ctx=Load()),
                            attr='call',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Constant(value='sudo', kind=None),
                                    Constant(value='mount', kind=None),
                                    Constant(value='-o', kind=None),
                                    Constant(value='remount,rw', kind=None),
                                    Constant(value='/', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='path', ctx=Store())],
                    value=BinOp(
                        left=Call(
                            func=Attribute(
                                value=Name(id='Path', ctx=Load()),
                                attr='home',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                        op=Div(),
                        right=Name(id='filename', ctx=Load()),
                    ),
                    type_comment=None,
                ),
                If(
                    test=Call(
                        func=Attribute(
                            value=Name(id='path', ctx=Load()),
                            attr='exists',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='path', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='subprocess', ctx=Load()),
                            attr='call',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Constant(value='sudo', kind=None),
                                    Constant(value='mount', kind=None),
                                    Constant(value='-o', kind=None),
                                    Constant(value='remount,ro', kind=None),
                                    Constant(value='/', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='subprocess', ctx=Load()),
                            attr='call',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Constant(value='sudo', kind=None),
                                    Constant(value='mount', kind=None),
                                    Constant(value='-o', kind=None),
                                    Constant(value='remount,rw', kind=None),
                                    Constant(value='/root_bypass_ramdisks/etc/cups', kind=None),
                                ],
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
            name='write_file',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='filename', annotation=None, type_comment=None),
                    arg(arg='text', annotation=None, type_comment=None),
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
                            value=Name(id='subprocess', ctx=Load()),
                            attr='call',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Constant(value='sudo', kind=None),
                                    Constant(value='mount', kind=None),
                                    Constant(value='-o', kind=None),
                                    Constant(value='remount,rw', kind=None),
                                    Constant(value='/', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='path', ctx=Store())],
                    value=BinOp(
                        left=Call(
                            func=Attribute(
                                value=Name(id='Path', ctx=Load()),
                                attr='home',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                        op=Div(),
                        right=Name(id='filename', ctx=Load()),
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='path', ctx=Load()),
                            attr='write_text',
                            ctx=Load(),
                        ),
                        args=[Name(id='text', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='subprocess', ctx=Load()),
                            attr='call',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Constant(value='sudo', kind=None),
                                    Constant(value='mount', kind=None),
                                    Constant(value='-o', kind=None),
                                    Constant(value='remount,ro', kind=None),
                                    Constant(value='/', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='subprocess', ctx=Load()),
                            attr='call',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Constant(value='sudo', kind=None),
                                    Constant(value='mount', kind=None),
                                    Constant(value='-o', kind=None),
                                    Constant(value='remount,rw', kind=None),
                                    Constant(value='/root_bypass_ramdisks/etc/cups', kind=None),
                                ],
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
    ],
    type_ignores=[],
)
