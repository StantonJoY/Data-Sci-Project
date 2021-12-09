Module(
    body=[
        Import(
            names=[alias(name='argparse', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='pexpect', asname=None)],
        ),
        Import(
            names=[alias(name='shutil', asname=None)],
        ),
        Import(
            names=[alias(name='signal', asname=None)],
        ),
        Import(
            names=[alias(name='subprocess', asname=None)],
        ),
        Import(
            names=[alias(name='sys', asname=None)],
        ),
        Import(
            names=[alias(name='tempfile', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        Import(
            names=[alias(name='traceback', asname=None)],
        ),
        ImportFrom(
            module='xmlrpc',
            names=[alias(name='client', asname='xmlrpclib')],
            level=0,
        ),
        ImportFrom(
            module='glob',
            names=[alias(name='glob', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='ROOTDIR', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Attribute(
                        value=Name(id='os', ctx=Load()),
                        attr='path',
                        ctx=Load(),
                    ),
                    attr='dirname',
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
                            attr='dirname',
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
                                    attr='realpath',
                                    ctx=Load(),
                                ),
                                args=[Name(id='__file__', ctx=Load())],
                                keywords=[],
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
            targets=[Name(id='TSTAMP', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='time', ctx=Load()),
                    attr='strftime',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='%Y%m%d', kind=None),
                    Call(
                        func=Attribute(
                            value=Name(id='time', ctx=Load()),
                            attr='gmtime',
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
        Expr(
            value=Call(
                func=Name(id='exec', ctx=Load()),
                args=[
                    Call(
                        func=Attribute(
                            value=Call(
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
                                            Name(id='ROOTDIR', ctx=Load()),
                                            Constant(value='odoo', kind=None),
                                            Constant(value='release.py', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='rb', kind=None),
                                ],
                                keywords=[],
                            ),
                            attr='read',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ],
                keywords=[],
            ),
        ),
        Assign(
            targets=[Name(id='VERSION', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Subscript(
                        value=Call(
                            func=Attribute(
                                value=Name(id='version', ctx=Load()),
                                attr='split',
                                ctx=Load(),
                            ),
                            args=[Constant(value='-', kind=None)],
                            keywords=[],
                        ),
                        slice=Constant(value=0, kind=None),
                        ctx=Load(),
                    ),
                    attr='replace',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='saas~', kind=None),
                    Constant(value='', kind=None),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='GPGPASSPHRASE', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='os', ctx=Load()),
                    attr='getenv',
                    ctx=Load(),
                ),
                args=[Constant(value='GPGPASSPHRASE', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='GPGID', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='os', ctx=Load()),
                    attr='getenv',
                    ctx=Load(),
                ),
                args=[Constant(value='GPGID', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DOCKERVERSION', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='VERSION', ctx=Load()),
                    attr='replace',
                    ctx=Load(),
                ),
                args=[
                    Constant(value='+', kind=None),
                    Constant(value='', kind=None),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='INSTALL_TIMEOUT', ctx=Store())],
            value=Constant(value=600, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DOCKERUSER', ctx=Store())],
            value=BinOp(
                left=Constant(value='\nRUN mkdir /var/lib/odoo &&     groupadd -g %(group_id)s odoo &&     useradd -u %(user_id)s -g odoo odoo -d /var/lib/odoo &&     mkdir /data &&     chown odoo:odoo /var/lib/odoo /data\nUSER odoo\n', kind=None),
                op=Mod(),
                right=Dict(
                    keys=[
                        Constant(value='group_id', kind=None),
                        Constant(value='user_id', kind=None),
                    ],
                    values=[
                        Call(
                            func=Attribute(
                                value=Name(id='os', ctx=Load()),
                                attr='getgid',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                        Call(
                            func=Attribute(
                                value=Name(id='os', ctx=Load()),
                                attr='getuid',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                    ],
                ),
            ),
            type_comment=None,
        ),
        ClassDef(
            name='OdooTestTimeoutError',
            bases=[Name(id='Exception', ctx=Load())],
            keywords=[],
            body=[Pass()],
            decorator_list=[],
        ),
        ClassDef(
            name='OdooTestError',
            bases=[Name(id='Exception', ctx=Load())],
            keywords=[],
            body=[Pass()],
            decorator_list=[],
        ),
        FunctionDef(
            name='run_cmd',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cmd', annotation=None, type_comment=None),
                    arg(arg='chdir', annotation=None, type_comment=None),
                    arg(arg='timeout', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='logging', ctx=Load()),
                            attr='info',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='Running command %s', kind=None),
                            Name(id='cmd', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='subprocess', ctx=Load()),
                            attr='run',
                            ctx=Load(),
                        ),
                        args=[Name(id='cmd', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='cwd',
                                value=Name(id='chdir', ctx=Load()),
                            ),
                            keyword(
                                arg='timeout',
                                value=Name(id='timeout', ctx=Load()),
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
            name='_rpc_count_modules',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='addr', annotation=None, type_comment=None),
                    arg(arg='port', annotation=None, type_comment=None),
                    arg(arg='dbname', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value='http://127.0.0.1', kind=None),
                    Constant(value=8069, kind=None),
                    Constant(value='mycompany', kind=None),
                ],
            ),
            body=[
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
                Assign(
                    targets=[Name(id='uid', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='xmlrpclib', ctx=Load()),
                                    attr='ServerProxy',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='%s:%s/xmlrpc/2/common', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='addr', ctx=Load()),
                                                Name(id='port', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            attr='authenticate',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='dbname', ctx=Load()),
                            Constant(value='admin', kind=None),
                            Constant(value='admin', kind=None),
                            Dict(keys=[], values=[]),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='modules', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='xmlrpclib', ctx=Load()),
                                    attr='ServerProxy',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='%s:%s/xmlrpc/2/object', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='addr', ctx=Load()),
                                                Name(id='port', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            attr='execute',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='dbname', ctx=Load()),
                            Name(id='uid', ctx=Load()),
                            Constant(value='admin', kind=None),
                            Constant(value='ir.module.module', kind=None),
                            Constant(value='search', kind=None),
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
                If(
                    test=Compare(
                        left=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[Name(id='modules', ctx=Load())],
                            keywords=[],
                        ),
                        ops=[Gt()],
                        comparators=[Constant(value=1, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='time', ctx=Load()),
                                    attr='sleep',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=1, kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='toinstallmodules', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='xmlrpclib', ctx=Load()),
                                            attr='ServerProxy',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='%s:%s/xmlrpc/2/object', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='addr', ctx=Load()),
                                                        Name(id='port', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='dbname', ctx=Load()),
                                    Name(id='uid', ctx=Load()),
                                    Constant(value='admin', kind=None),
                                    Constant(value='ir.module.module', kind=None),
                                    Constant(value='search', kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='state', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='to install', kind=None),
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
                        If(
                            test=Name(id='toinstallmodules', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='logging', ctx=Load()),
                                            attr='error',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='Package test: FAILED. Not able to install dependencies of base.', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id='OdooTestError', ctx=Load()),
                                        args=[Constant(value='Installation of package failed', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='logging', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='Package test: successfuly installed %s modules', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='modules', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    orelse=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='error',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Package test: FAILED. Not able to install base.', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Raise(
                            exc=Call(
                                func=Name(id='OdooTestError', ctx=Load()),
                                args=[Constant(value='Package test: FAILED. Not able to install base.', kind=None)],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='publish',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='args', annotation=None, type_comment=None),
                    arg(arg='pub_type', annotation=None, type_comment=None),
                    arg(arg='extensions', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Publish builded package (move builded files and generate a symlink to the latests)\n    :args: parsed program args\n    :pub_type: one of [deb, rpm, src, exe]\n    :extensions: list of extensions to publish\n    :returns: published files\n    ', kind=None),
                ),
                FunctionDef(
                    name='_publish',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='release', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='build_path', ctx=Store())],
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
                                    Attribute(
                                        value=Name(id='args', ctx=Load()),
                                        attr='build_dir',
                                        ctx=Load(),
                                    ),
                                    Name(id='release', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='filename', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='release', ctx=Load()),
                                        attr='split',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='sep',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=UnaryOp(
                                    op=USub(),
                                    operand=Constant(value=1, kind=None),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='release_dir', ctx=Store())],
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
                                    Attribute(
                                        value=Name(id='args', ctx=Load()),
                                        attr='pub',
                                        ctx=Load(),
                                    ),
                                    Name(id='pub_type', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='release_path', ctx=Store())],
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
                                    Name(id='release_dir', ctx=Load()),
                                    Name(id='filename', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='renames',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='build_path', ctx=Load()),
                                    Name(id='release_path', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='release_abspath', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='abspath',
                                    ctx=Load(),
                                ),
                                args=[Name(id='release_path', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='latest_abspath', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='release_abspath', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='TSTAMP', ctx=Load()),
                                    Constant(value='latest', kind=None),
                                ],
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
                                    attr='islink',
                                    ctx=Load(),
                                ),
                                args=[Name(id='latest_abspath', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='latest_abspath', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='symlink',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='release_abspath', ctx=Load()),
                                    Name(id='latest_abspath', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='release_path', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='published', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                For(
                    target=Name(id='extension', ctx=Store()),
                    iter=Name(id='extensions', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='release', ctx=Store())],
                            value=Call(
                                func=Name(id='glob', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='%s/odoo_*.%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='args', ctx=Load()),
                                                    attr='build_dir',
                                                    ctx=Load(),
                                                ),
                                                Name(id='extension', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='release', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='published', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_publish', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='release', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
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
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Name(id='published', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='gen_deb_package',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='args', annotation=None, type_comment=None),
                    arg(arg='published_files', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                FunctionDef(
                    name='_gen_file',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='args', annotation=None, type_comment=None),
                            arg(arg='command', annotation=None, type_comment=None),
                            arg(arg='file_name', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='cur_tmp_file_path', ctx=Store())],
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
                                    Name(id='file_name', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='open', ctx=Load()),
                                        args=[
                                            Name(id='cur_tmp_file_path', ctx=Load()),
                                            Constant(value='w', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='out', ctx=Store()),
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='subprocess', ctx=Load()),
                                            attr='call',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='command', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='stdout',
                                                value=Name(id='out', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='cwd',
                                                value=Name(id='path', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='shutil', ctx=Load()),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='cur_tmp_file_path', ctx=Load()),
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
                                            Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='pub',
                                                ctx=Load(),
                                            ),
                                            Constant(value='deb', kind=None),
                                            Name(id='file_name', ctx=Load()),
                                        ],
                                        keywords=[],
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
                Assign(
                    targets=[Name(id='temp_path', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='tempfile', ctx=Load()),
                            attr='mkdtemp',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='suffix',
                                value=Constant(value='debPackages', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='pub_file_path', ctx=Store()),
                    iter=Name(id='published_files', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='shutil', ctx=Load()),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='pub_file_path', ctx=Load()),
                                    Name(id='temp_path', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='commands', ctx=Store())],
                    value=List(
                        elts=[
                            Tuple(
                                elts=[
                                    List(
                                        elts=[
                                            Constant(value='dpkg-scanpackages', kind=None),
                                            Constant(value='--multiversion', kind=None),
                                            Constant(value='.', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='Packages', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            Tuple(
                                elts=[
                                    List(
                                        elts=[
                                            Constant(value='dpkg-scansources', kind=None),
                                            Constant(value='.', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='Sources', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            Tuple(
                                elts=[
                                    List(
                                        elts=[
                                            Constant(value='apt-ftparchive', kind=None),
                                            Constant(value='release', kind=None),
                                            Constant(value='.', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='Release', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='command', ctx=Store()),
                    iter=Name(id='commands', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='_gen_file', ctx=Load()),
                                args=[
                                    Name(id='args', ctx=Load()),
                                    Subscript(
                                        value=Name(id='command', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='command', ctx=Load()),
                                        slice=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=1, kind=None),
                                        ),
                                        ctx=Load(),
                                    ),
                                    Name(id='temp_path', ctx=Load()),
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
                            value=Name(id='shutil', ctx=Load()),
                            attr='rmtree',
                            ctx=Load(),
                        ),
                        args=[Name(id='temp_path', ctx=Load())],
                        keywords=[],
                    ),
                ),
                If(
                    test=Attribute(
                        value=Name(id='args', ctx=Load()),
                        attr='sign',
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
                                            Constant(value='gpg', kind=None),
                                            Constant(value='--default-key', kind=None),
                                            Name(id='GPGID', ctx=Load()),
                                            Constant(value='--passphrase', kind=None),
                                            Name(id='GPGPASSPHRASE', ctx=Load()),
                                            Constant(value='--yes', kind=None),
                                            Constant(value='-abs', kind=None),
                                            Constant(value='--no-tty', kind=None),
                                            Constant(value='-o', kind=None),
                                            Constant(value='Release.gpg', kind=None),
                                            Constant(value='Release', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='cwd',
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
                                                Attribute(
                                                    value=Name(id='args', ctx=Load()),
                                                    attr='pub',
                                                    ctx=Load(),
                                                ),
                                                Constant(value='deb', kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
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
            name='rpm_sign',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='args', annotation=None, type_comment=None),
                    arg(arg='file_name', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Genereate a rpm repo in publish directory', kind=None),
                ),
                Assign(
                    targets=[Name(id='rpmsign', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='pexpect', ctx=Load()),
                            attr='spawn',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='/bin/bash', kind=None),
                            List(
                                elts=[
                                    Constant(value='-c', kind=None),
                                    BinOp(
                                        left=Constant(value='rpm --resign %s', kind=None),
                                        op=Mod(),
                                        right=Name(id='file_name', ctx=Load()),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='cwd',
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
                                        Attribute(
                                            value=Name(id='args', ctx=Load()),
                                            attr='pub',
                                            ctx=Load(),
                                        ),
                                        Constant(value='rpm', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='rpmsign', ctx=Load()),
                            attr='expect_exact',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Enter passphrase: ', kind=None)],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='rpmsign', ctx=Load()),
                            attr='send',
                            ctx=Load(),
                        ),
                        args=[
                            BinOp(
                                left=Name(id='GPGPASSPHRASE', ctx=Load()),
                                op=Add(),
                                right=Constant(value='\r\n', kind=None),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='rpmsign', ctx=Load()),
                            attr='expect',
                            ctx=Load(),
                        ),
                        args=[
                            Attribute(
                                value=Name(id='pexpect', ctx=Load()),
                                attr='EOF',
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
            name='_prepare_build_dir',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='args', annotation=None, type_comment=None),
                    arg(arg='win32', annotation=None, type_comment=None),
                    arg(arg='move_addons', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=False, kind=None),
                    Constant(value=True, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value='Copy files to the build directory', kind=None),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='logging', ctx=Load()),
                            attr='info',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='Preparing build dir "%s"', kind=None),
                            Attribute(
                                value=Name(id='args', ctx=Load()),
                                attr='build_dir',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='cmd', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='rsync', kind=None),
                            Constant(value='-a', kind=None),
                            Constant(value='--delete', kind=None),
                            Constant(value='--exclude', kind=None),
                            Constant(value='.git', kind=None),
                            Constant(value='--exclude', kind=None),
                            Constant(value='*.pyc', kind=None),
                            Constant(value='--exclude', kind=None),
                            Constant(value='*.pyo', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='win32', ctx=Load()),
                        ops=[Is()],
                        comparators=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        AugAssign(
                            target=Name(id='cmd', ctx=Store()),
                            op=Add(),
                            value=List(
                                elts=[
                                    Constant(value='--exclude', kind=None),
                                    Constant(value='setup/win32', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Expr(
                    value=Call(
                        func=Name(id='run_cmd', ctx=Load()),
                        args=[
                            BinOp(
                                left=Name(id='cmd', ctx=Load()),
                                op=Add(),
                                right=List(
                                    elts=[
                                        BinOp(
                                            left=Constant(value='%s/', kind=None),
                                            op=Mod(),
                                            right=Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='odoo_dir',
                                                ctx=Load(),
                                            ),
                                        ),
                                        Attribute(
                                            value=Name(id='args', ctx=Load()),
                                            attr='build_dir',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='move_addons', ctx=Load()),
                    ),
                    body=[Return(value=None)],
                    orelse=[],
                ),
                For(
                    target=Name(id='addon_path', ctx=Store()),
                    iter=Call(
                        func=Name(id='glob', ctx=Load()),
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
                                    Attribute(
                                        value=Name(id='args', ctx=Load()),
                                        attr='build_dir',
                                        ctx=Load(),
                                    ),
                                    Constant(value='addons/*', kind=None),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='args', ctx=Load()),
                                            attr='blacklist',
                                            ctx=Load(),
                                        ),
                                        ops=[Is()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='path',
                                                    ctx=Load(),
                                                ),
                                                attr='basename',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='addon_path', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[NotIn()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='blacklist',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='shutil', ctx=Load()),
                                                    attr='move',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='addon_path', ctx=Load()),
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
                                                            Attribute(
                                                                value=Name(id='args', ctx=Load()),
                                                                attr='build_dir',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='odoo/addons', kind=None),
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
                                            type=Attribute(
                                                value=Name(id='shutil', ctx=Load()),
                                                attr='Error',
                                                ctx=Load(),
                                            ),
                                            name='e',
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='logging', ctx=Load()),
                                                            attr='warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value="Warning '%s' while moving addon '%s", kind=None),
                                                            Name(id='e', ctx=Load()),
                                                            Name(id='addon_path', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='addon_path', ctx=Load()),
                                                                    attr='startswith',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='args', ctx=Load()),
                                                                        attr='build_dir',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='os', ctx=Load()),
                                                                        attr='path',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='isdir',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='addon_path', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='logging', ctx=Load()),
                                                                    attr='info',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Constant(value="Removing '{}'", kind=None),
                                                                            attr='format',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='addon_path', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Try(
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='shutil', ctx=Load()),
                                                                            attr='rmtree',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='addon_path', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            handlers=[
                                                                ExceptHandler(
                                                                    type=Attribute(
                                                                        value=Name(id='shutil', ctx=Load()),
                                                                        attr='Error',
                                                                        ctx=Load(),
                                                                    ),
                                                                    name='rm_error',
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='logging', ctx=Load()),
                                                                                    attr='warning',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Constant(value="Cannot remove '{}': {}", kind=None),
                                                                                            attr='format',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Name(id='addon_path', ctx=Load()),
                                                                                            Name(id='rm_error', ctx=Load()),
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
                                                            orelse=[],
                                                            finalbody=[],
                                                        ),
                                                    ],
                                                    orelse=[],
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
                    orelse=[],
                    type_comment=None,
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='Docker',
            bases=[],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Base Docker class. Must be inherited by specific Docker builder class', kind=None),
                ),
                Assign(
                    targets=[Name(id='arch', ctx=Store())],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='args', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        :param args: argparse parsed arguments\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='args',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='args', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='tag',
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=Constant(value='odoo-%s-%s-nightly-tests', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='DOCKERVERSION', ctx=Load()),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='arch',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='container_name',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='exposed_port',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dockerfiles', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='tgz', kind=None),
                                    Constant(value='deb', kind=None),
                                    Constant(value='rpm', kind=None),
                                ],
                                values=[
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
                                            Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='build_dir',
                                                ctx=Load(),
                                            ),
                                            Constant(value='setup/package.dfsrc', kind=None),
                                        ],
                                        keywords=[],
                                    ),
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
                                            Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='build_dir',
                                                ctx=Load(),
                                            ),
                                            Constant(value='setup/package.dfdebian', kind=None),
                                        ],
                                        keywords=[],
                                    ),
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
                                            Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='build_dir',
                                                ctx=Load(),
                                            ),
                                            Constant(value='setup/package.dffedora', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='dockerfile',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Name(id='dockerfiles', ctx=Load()),
                                slice=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='arch',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='test_log_file',
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=Constant(value='/data/src/test-%s.log', kind=None),
                                op=Mod(),
                                right=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='arch',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='build_image',
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
                    name='build_image',
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
                            value=Constant(value='Build the dockerimage by copying Dockerfile into build_dir/docker', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='docker_dir', ctx=Store())],
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='args',
                                            ctx=Load(),
                                        ),
                                        attr='build_dir',
                                        ctx=Load(),
                                    ),
                                    Constant(value='docker', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='docker_file_path', ctx=Store())],
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
                                    Name(id='docker_dir', ctx=Load()),
                                    Constant(value='Dockerfile', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='mkdir',
                                    ctx=Load(),
                                ),
                                args=[Name(id='docker_dir', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='shutil', ctx=Load()),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='dockerfile',
                                        ctx=Load(),
                                    ),
                                    Name(id='docker_file_path', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='open', ctx=Load()),
                                        args=[
                                            Name(id='docker_file_path', ctx=Load()),
                                            Constant(value='a', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='dockerfile', ctx=Store()),
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='dockerfile', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='DOCKERUSER', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='shutil', ctx=Load()),
                                    attr='copy',
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
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='args',
                                                    ctx=Load(),
                                                ),
                                                attr='build_dir',
                                                ctx=Load(),
                                            ),
                                            Constant(value='requirements.txt', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='docker_dir', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='run_cmd', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='docker', kind=None),
                                                    Constant(value='build', kind=None),
                                                    Constant(value='--rm=True', kind=None),
                                                    Constant(value='-t', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tag',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='.', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='chdir',
                                                value=Name(id='docker_dir', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='timeout',
                                                value=Constant(value=1200, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='check_returncode',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='shutil', ctx=Load()),
                                    attr='rmtree',
                                    ctx=Load(),
                                ),
                                args=[Name(id='docker_dir', ctx=Load())],
                                keywords=[],
                            ),
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
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='cmd', annotation=None, type_comment=None),
                            arg(arg='build_dir', annotation=None, type_comment=None),
                            arg(arg='container_name', annotation=None, type_comment=None),
                            arg(arg='user', annotation=None, type_comment=None),
                            arg(arg='exposed_port', annotation=None, type_comment=None),
                            arg(arg='detach', annotation=None, type_comment=None),
                            arg(arg='timeout', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value='odoo', kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='container_name',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='container_name', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='docker_cmd', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='docker', kind=None),
                                    Constant(value='run', kind=None),
                                    BinOp(
                                        left=Constant(value='--user=%s', kind=None),
                                        op=Mod(),
                                        right=Name(id='user', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Constant(value='--name=%s', kind=None),
                                        op=Mod(),
                                        right=Name(id='container_name', ctx=Load()),
                                    ),
                                    Constant(value='--rm', kind=None),
                                    BinOp(
                                        left=Constant(value='--volume=%s:/data/src', kind=None),
                                        op=Mod(),
                                        right=Name(id='build_dir', ctx=Load()),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='exposed_port', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='docker_cmd', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='-p', kind=None),
                                                    BinOp(
                                                        left=Constant(value='127.0.0.1:%s:%s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='exposed_port', ctx=Load()),
                                                                Name(id='exposed_port', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='exposed_port',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='exposed_port', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='detach', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='docker_cmd', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='-d', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='cmd', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='(%s) > %s 2>&1', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='cmd', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='test_log_file',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='docker_cmd', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tag',
                                                ctx=Load(),
                                            ),
                                            Constant(value='/bin/bash', kind=None),
                                            Constant(value='-c', kind=None),
                                            BinOp(
                                                left=Constant(value='cd /data/src && %s', kind=None),
                                                op=Mod(),
                                                right=Name(id='cmd', ctx=Load()),
                                            ),
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
                                        func=Name(id='run_cmd', ctx=Load()),
                                        args=[Name(id='docker_cmd', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='timeout',
                                                value=Name(id='timeout', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    attr='check_returncode',
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
                    name='is_running',
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
                            targets=[Name(id='dinspect', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='run',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='docker', kind=None),
                                            Constant(value='container', kind=None),
                                            Constant(value='inspect', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='container_name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='stderr',
                                        value=Attribute(
                                            value=Name(id='subprocess', ctx=Load()),
                                            attr='DEVNULL',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='stdout',
                                        value=Attribute(
                                            value=Name(id='subprocess', ctx=Load()),
                                            attr='DEVNULL',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=IfExp(
                                test=Compare(
                                    left=Attribute(
                                        value=Name(id='dinspect', ctx=Load()),
                                        attr='returncode',
                                        ctx=Load(),
                                    ),
                                    ops=[Eq()],
                                    comparators=[Constant(value=0, kind=None)],
                                ),
                                body=Constant(value=True, kind=None),
                                orelse=Constant(value=False, kind=None),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='stop',
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
                                    value=Call(
                                        func=Name(id='run_cmd', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='docker', kind=None),
                                                    Constant(value='stop', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='container_name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='check_returncode',
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
                    name='test_odoo',
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
                                    value=Name(id='logging', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Starting to test Odoo install test', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='start_time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='time', ctx=Load()),
                                    attr='time',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        While(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='is_running',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=BinOp(
                                            left=Call(
                                                func=Attribute(
                                                    value=Name(id='time', ctx=Load()),
                                                    attr='time',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            op=Sub(),
                                            right=Name(id='start_time', ctx=Load()),
                                        ),
                                        ops=[Lt()],
                                        comparators=[Name(id='INSTALL_TIMEOUT', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
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
                                                    Attribute(
                                                        value=Name(id='args', ctx=Load()),
                                                        attr='build_dir',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='odoo.pid', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Try(
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='_rpc_count_modules', ctx=Load()),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='port',
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='exposed_port',
                                                                    ctx=Load(),
                                                                ),
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
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='stop',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Return(value=None),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='is_running',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='stop',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id='OdooTestTimeoutError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='Odoo pid file never appeared after %s sec', kind=None),
                                                op=Mod(),
                                                right=Name(id='INSTALL_TIMEOUT', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Raise(
                            exc=Call(
                                func=Name(id='OdooTestError', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='Error while installing/starting Odoo after %s sec.\nSee testlogs.txt in build dir', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Name(id='int', ctx=Load()),
                                            args=[
                                                BinOp(
                                                    left=Call(
                                                        func=Attribute(
                                                            value=Name(id='time', ctx=Load()),
                                                            attr='time',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    op=Sub(),
                                                    right=Name(id='start_time', ctx=Load()),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
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
                    name='build',
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
                            value=Constant(value='To be overriden by specific builder', kind=None),
                        ),
                        Pass(),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='start_test',
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
                            value=Constant(value='To be overriden by specific builder', kind=None),
                        ),
                        Pass(),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='DockerTgz',
            bases=[Name(id='Docker', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Docker class to build python src package', kind=None),
                ),
                Assign(
                    targets=[Name(id='arch', ctx=Store())],
                    value=Constant(value='tgz', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='build',
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
                                    value=Name(id='logging', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Start building python tgz package', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='run',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='python3 setup.py sdist --quiet --formats=gztar,zip', kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='args',
                                            ctx=Load(),
                                        ),
                                        attr='build_dir',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='odoo-src-build-%s', kind=None),
                                        op=Mod(),
                                        right=Name(id='TSTAMP', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='rename',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Name(id='glob', ctx=Load()),
                                            args=[
                                                BinOp(
                                                    left=Constant(value='%s/dist/odoo-*.tar.gz', kind=None),
                                                    op=Mod(),
                                                    right=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='args',
                                                            ctx=Load(),
                                                        ),
                                                        attr='build_dir',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s/odoo_%s.%s.tar.gz', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='args',
                                                        ctx=Load(),
                                                    ),
                                                    attr='build_dir',
                                                    ctx=Load(),
                                                ),
                                                Name(id='VERSION', ctx=Load()),
                                                Name(id='TSTAMP', ctx=Load()),
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
                                    attr='rename',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Name(id='glob', ctx=Load()),
                                            args=[
                                                BinOp(
                                                    left=Constant(value='%s/dist/odoo-*.zip', kind=None),
                                                    op=Mod(),
                                                    right=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='args',
                                                            ctx=Load(),
                                                        ),
                                                        attr='build_dir',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s/odoo_%s.%s.zip', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='args',
                                                        ctx=Load(),
                                                    ),
                                                    attr='build_dir',
                                                    ctx=Load(),
                                                ),
                                                Name(id='VERSION', ctx=Load()),
                                                Name(id='TSTAMP', ctx=Load()),
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
                                    value=Name(id='logging', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Finished building python tgz package', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='start_test',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='args',
                                        ctx=Load(),
                                    ),
                                    attr='test',
                                    ctx=Load(),
                                ),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Start testing python tgz package', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='cmds', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='service postgresql start', kind=None),
                                    BinOp(
                                        left=Constant(value='pip3 install /data/src/odoo_%s.%s.tar.gz', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='VERSION', ctx=Load()),
                                                Name(id='TSTAMP', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value='su postgres -s /bin/bash -c "createuser -s odoo"', kind=None),
                                    Constant(value='su postgres -s /bin/bash -c "createdb mycompany"', kind=None),
                                    Constant(value='su odoo -s /bin/bash -c "odoo -d mycompany -i base --stop-after-init"', kind=None),
                                    Constant(value='su odoo -s /bin/bash -c "odoo -d mycompany --pidfile=/data/src/odoo.pid"', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='run',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value=' && ', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='cmds', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='args',
                                            ctx=Load(),
                                        ),
                                        attr='build_dir',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='odoo-src-test-%s', kind=None),
                                        op=Mod(),
                                        right=Name(id='TSTAMP', ctx=Load()),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='user',
                                        value=Constant(value='root', kind=None),
                                    ),
                                    keyword(
                                        arg='detach',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='exposed_port',
                                        value=Constant(value=8069, kind=None),
                                    ),
                                    keyword(
                                        arg='timeout',
                                        value=Constant(value=300, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='test_odoo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Finished testing tgz package', kind=None)],
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
        ClassDef(
            name='DockerDeb',
            bases=[Name(id='Docker', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Docker class to build debian package', kind=None),
                ),
                Assign(
                    targets=[Name(id='arch', ctx=Store())],
                    value=Constant(value='deb', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='build',
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
                                    value=Name(id='logging', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Start building debian package', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='cmds', ctx=Store())],
                            value=List(
                                elts=[
                                    BinOp(
                                        left=Constant(value="sed -i '1s/^.*$/odoo (%s.%s) stable; urgency=low/' debian/changelog", kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='VERSION', ctx=Load()),
                                                Name(id='TSTAMP', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cmds', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='dpkg-buildpackage -rfakeroot -uc -us -tc', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cmds', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='mv ../odoo_* ./', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='run',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value=' && ', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='cmds', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='args',
                                            ctx=Load(),
                                        ),
                                        attr='build_dir',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='odoo-deb-build-%s', kind=None),
                                        op=Mod(),
                                        right=Name(id='TSTAMP', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Finished building debian package', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='start_test',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='args',
                                        ctx=Load(),
                                    ),
                                    attr='test',
                                    ctx=Load(),
                                ),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Start testing debian package', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='cmds', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='service postgresql start', kind=None),
                                    Constant(value='su postgres -s /bin/bash -c "createdb mycompany"', kind=None),
                                    Constant(value='/usr/bin/apt-get update -y', kind=None),
                                    BinOp(
                                        left=Constant(value='/usr/bin/dpkg -i /data/src/odoo_%s.%s_all.deb ; /usr/bin/apt-get install -f -y', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='VERSION', ctx=Load()),
                                                Name(id='TSTAMP', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value='su odoo -s /bin/bash -c "odoo -d mycompany -i base --stop-after-init"', kind=None),
                                    Constant(value='su odoo -s /bin/bash -c "odoo -d mycompany --pidfile=/data/src/odoo.pid"', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='run',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value=' && ', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='cmds', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='args',
                                            ctx=Load(),
                                        ),
                                        attr='build_dir',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='odoo-deb-test-%s', kind=None),
                                        op=Mod(),
                                        right=Name(id='TSTAMP', ctx=Load()),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='user',
                                        value=Constant(value='root', kind=None),
                                    ),
                                    keyword(
                                        arg='detach',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='exposed_port',
                                        value=Constant(value=8069, kind=None),
                                    ),
                                    keyword(
                                        arg='timeout',
                                        value=Constant(value=300, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='test_odoo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Finished testing debian package', kind=None)],
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
        ClassDef(
            name='DockerRpm',
            bases=[Name(id='Docker', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Docker class to build rpm package', kind=None),
                ),
                Assign(
                    targets=[Name(id='arch', ctx=Store())],
                    value=Constant(value='rpm', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='build',
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
                                    value=Name(id='logging', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Start building fedora rpm package', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='run',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='python3 setup.py --quiet bdist_rpm', kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='args',
                                            ctx=Load(),
                                        ),
                                        attr='build_dir',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='odoo-rpm-build-%s', kind=None),
                                        op=Mod(),
                                        right=Name(id='TSTAMP', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='rename',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Name(id='glob', ctx=Load()),
                                            args=[
                                                BinOp(
                                                    left=Constant(value='%s/dist/odoo-*.noarch.rpm', kind=None),
                                                    op=Mod(),
                                                    right=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='args',
                                                            ctx=Load(),
                                                        ),
                                                        attr='build_dir',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s/odoo_%s.%s.rpm', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='args',
                                                        ctx=Load(),
                                                    ),
                                                    attr='build_dir',
                                                    ctx=Load(),
                                                ),
                                                Name(id='VERSION', ctx=Load()),
                                                Name(id='TSTAMP', ctx=Load()),
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
                                    value=Name(id='logging', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Finished building fedora rpm package', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='start_test',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='args',
                                        ctx=Load(),
                                    ),
                                    attr='test',
                                    ctx=Load(),
                                ),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Start testing rpm package', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='cmds', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='su postgres -c "/usr/bin/pg_ctl -D /var/lib/postgres/data start"', kind=None),
                                    Constant(value='sleep 5', kind=None),
                                    Constant(value='su postgres -c "createdb mycompany"', kind=None),
                                    BinOp(
                                        left=Constant(value='dnf install -d 0 -e 0 /data/src/odoo_%s.%s.rpm -y', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='VERSION', ctx=Load()),
                                                Name(id='TSTAMP', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value='su odoo -s /bin/bash -c "odoo -c /etc/odoo/odoo.conf -d mycompany -i base --stop-after-init"', kind=None),
                                    Constant(value='su odoo -s /bin/bash -c "odoo -c /etc/odoo/odoo.conf -d mycompany --pidfile=/data/src/odoo.pid"', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='run',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value=' && ', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='cmds', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='args', ctx=Load()),
                                        attr='build_dir',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='odoo-rpm-test-%s', kind=None),
                                        op=Mod(),
                                        right=Name(id='TSTAMP', ctx=Load()),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='user',
                                        value=Constant(value='root', kind=None),
                                    ),
                                    keyword(
                                        arg='detach',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='exposed_port',
                                        value=Constant(value=8069, kind=None),
                                    ),
                                    keyword(
                                        arg='timeout',
                                        value=Constant(value=300, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='test_odoo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Finished testing rpm package', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='gen_rpm_repo',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='args', annotation=None, type_comment=None),
                            arg(arg='rpm_filepath', annotation=None, type_comment=None),
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
                                    value=Name(id='shutil', ctx=Load()),
                                    attr='rmtree',
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
                                            Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='pub',
                                                ctx=Load(),
                                            ),
                                            Constant(value='rpm', kind=None),
                                            Constant(value='repodata', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='temp_path', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tempfile', ctx=Load()),
                                    attr='mkdtemp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='suffix',
                                        value=Constant(value='rpmPackages', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='shutil', ctx=Load()),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='rpm_filepath', ctx=Load()),
                                    Name(id='temp_path', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Start creating rpm repo', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='run',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='createrepo /data/src/', kind=None),
                                    Name(id='temp_path', ctx=Load()),
                                    BinOp(
                                        left=Constant(value='odoo-rpm-createrepo-%s', kind=None),
                                        op=Mod(),
                                        right=Name(id='TSTAMP', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='shutil', ctx=Load()),
                                    attr='copytree',
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
                                            Name(id='temp_path', ctx=Load()),
                                            Constant(value='repodata', kind=None),
                                        ],
                                        keywords=[],
                                    ),
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
                                            Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='pub',
                                                ctx=Load(),
                                            ),
                                            Constant(value='rpm', kind=None),
                                            Constant(value='repodata', kind=None),
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
                                    value=Name(id='shutil', ctx=Load()),
                                    attr='rmtree',
                                    ctx=Load(),
                                ),
                                args=[Name(id='temp_path', ctx=Load())],
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
        ClassDef(
            name='KVM',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='args', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='args',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='args', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='image',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='args', ctx=Load()),
                                attr='vm_winxp_image',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ssh_key',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='args', ctx=Load()),
                                attr='vm_winxp_ssh_key',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='login',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='args', ctx=Load()),
                                attr='vm_winxp_login',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='timeout',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='signum', annotation=None, type_comment=None),
                            arg(arg='frame', annotation=None, type_comment=None),
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
                                    value=Name(id='logging', ctx=Load()),
                                    attr='warning',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value='vm timeout kill (pid: {})', kind=None),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='kvm_proc',
                                                    ctx=Load(),
                                                ),
                                                attr='pid',
                                                ctx=Load(),
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='kvm_proc',
                                        ctx=Load(),
                                    ),
                                    attr='terminate',
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
                    name='start',
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
                            targets=[Name(id='kvm_cmd', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='kvm', kind=None),
                                    Constant(value='-cpu', kind=None),
                                    Constant(value='Skylake-Client,hypervisor=on,hle=off,rtm=off', kind=None),
                                    Constant(value='-smp', kind=None),
                                    Constant(value='2,sockets=2,cores=1,threads=1', kind=None),
                                    Constant(value='-net', kind=None),
                                    Constant(value='nic,model=e1000e,macaddr=52:54:00:d3:38:5e', kind=None),
                                    Constant(value='-net', kind=None),
                                    Constant(value='user,hostfwd=tcp:127.0.0.1:10022-:22,hostfwd=tcp:127.0.0.1:18069-:8069,hostfwd=tcp:127.0.0.1:15432-:5432', kind=None),
                                    Constant(value='-m', kind=None),
                                    Constant(value='2048', kind=None),
                                    Constant(value='-drive', kind=None),
                                    BinOp(
                                        left=Constant(value='file=%s,snapshot=on', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='image',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value='-nographic', kind=None),
                                    Constant(value='-serial', kind=None),
                                    Constant(value='none', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value='Starting kvm: {}', kind=None),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value=' ', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='kvm_cmd', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='kvm_proc',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='subprocess', ctx=Load()),
                                    attr='Popen',
                                    ctx=Load(),
                                ),
                                args=[Name(id='kvm_cmd', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='wait_ssh',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=30, kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='signal', ctx=Load()),
                                            attr='alarm',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=2400, kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='signal', ctx=Load()),
                                            attr='signal',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='signal', ctx=Load()),
                                                attr='SIGALRM',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='timeout',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='run',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[],
                            orelse=[],
                            finalbody=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='signal', ctx=Load()),
                                            attr='signal',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='signal', ctx=Load()),
                                                attr='SIGALRM',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='signal', ctx=Load()),
                                                attr='SIG_DFL',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='kvm_proc',
                                                ctx=Load(),
                                            ),
                                            attr='terminate',
                                            ctx=Load(),
                                        ),
                                        args=[],
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
                                        args=[Constant(value=10, kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='ssh',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='cmd', annotation=None, type_comment=None),
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
                                    value=Call(
                                        func=Name(id='run_cmd', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='ssh', kind=None),
                                                    Constant(value='-o', kind=None),
                                                    Constant(value='UserKnownHostsFile=/dev/null', kind=None),
                                                    Constant(value='-o', kind=None),
                                                    Constant(value='StrictHostKeyChecking=no', kind=None),
                                                    Constant(value='-o', kind=None),
                                                    Constant(value='BatchMode=yes', kind=None),
                                                    Constant(value='-o', kind=None),
                                                    Constant(value='ConnectTimeout=10', kind=None),
                                                    Constant(value='-p', kind=None),
                                                    Constant(value='10022', kind=None),
                                                    Constant(value='-i', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='ssh_key',
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=Constant(value='%s@127.0.0.1', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='login',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Name(id='cmd', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='check_returncode',
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
                    name='rsync',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='rsync_args', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            List(
                                elts=[
                                    Constant(value='--delete', kind=None),
                                    Constant(value='--exclude', kind=None),
                                    Constant(value='.git', kind=None),
                                    Constant(value='--exclude', kind=None),
                                    Constant(value='.tx', kind=None),
                                    Constant(value='--exclude', kind=None),
                                    Constant(value='__pycache__', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='cmd', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='rsync', kind=None),
                                    Constant(value='-a', kind=None),
                                    Constant(value='-e', kind=None),
                                    BinOp(
                                        left=Constant(value='ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -p 10022 -i %s', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='ssh_key',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cmd', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[Name(id='options', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cmd', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[Name(id='rsync_args', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='run_cmd', ctx=Load()),
                                        args=[Name(id='cmd', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='check_returncode',
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
                    name='wait_ssh',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='n', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[Name(id='n', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='ssh',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='exit', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        Return(value=None),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Attribute(
                                                value=Name(id='subprocess', ctx=Load()),
                                                attr='CalledProcessError',
                                                ctx=Load(),
                                            ),
                                            name=None,
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='time', ctx=Load()),
                                                            attr='sleep',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=10, kind=None)],
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
                            type_comment=None,
                        ),
                        Raise(
                            exc=Call(
                                func=Name(id='Exception', ctx=Load()),
                                args=[Constant(value='Unable to conncect to the VM', kind=None)],
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
                    body=[Pass()],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='KVMWinBuildExe',
            bases=[Name(id='KVM', ctx=Load())],
            keywords=[],
            body=[
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
                                    value=Name(id='logging', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Start building Windows package', kind=None)],
                                keywords=[],
                            ),
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
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='args',
                                                            ctx=Load(),
                                                        ),
                                                        attr='build_dir',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='setup/win32/Makefile.version', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value='w', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='f', ctx=Store()),
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='f', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='VERSION=%s.%s\n', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='VERSION', ctx=Load()),
                                                                        attr='replace',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Constant(value='~', kind=None),
                                                                        Constant(value='_', kind=None),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                attr='replace',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Constant(value='+', kind=None),
                                                                Constant(value='', kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        Name(id='TSTAMP', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
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
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='args',
                                                            ctx=Load(),
                                                        ),
                                                        attr='build_dir',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='setup/win32/Makefile.python', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value='w', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='f', ctx=Store()),
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='f', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='PYTHON_VERSION=%s\n', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='args',
                                                        ctx=Load(),
                                                    ),
                                                    attr='vm_winxp_python_version',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
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
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='args',
                                                            ctx=Load(),
                                                        ),
                                                        attr='build_dir',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='setup/win32/Makefile.servicename', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value='w', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='f', ctx=Store()),
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='f', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='SERVICENAME=%s\n', kind=None),
                                                op=Mod(),
                                                right=Name(id='nt_service_name', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='remote_build_dir', ctx=Store())],
                            value=Constant(value='/cygdrive/c/odoobuild/server/', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ssh',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='mkdir -p build', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Syncing Odoo files to virtual machine...', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rsync',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='%s/', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='args',
                                                        ctx=Load(),
                                                    ),
                                                    attr='build_dir',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            BinOp(
                                                left=Constant(value='%s@127.0.0.1:%s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='login',
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='remote_build_dir', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='ssh',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value='cd {}setup/win32;time make allinone;', kind=None),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='remote_build_dir', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rsync',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='%s@127.0.0.1:%ssetup/win32/release/', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='login',
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='remote_build_dir', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            BinOp(
                                                left=Constant(value='%s/', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='args',
                                                        ctx=Load(),
                                                    ),
                                                    attr='build_dir',
                                                    ctx=Load(),
                                                ),
                                            ),
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
                                    value=Name(id='logging', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Finished building Windows package', kind=None)],
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
        ClassDef(
            name='KVMWinTestExe',
            bases=[Name(id='KVM', ctx=Load())],
            keywords=[],
            body=[
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
                                    value=Name(id='logging', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Start testing Windows package', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='setup_path', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Name(id='glob', ctx=Load()),
                                    args=[
                                        BinOp(
                                            left=Constant(value='%s/odoo_setup_*.exe', kind=None),
                                            op=Mod(),
                                            right=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='args',
                                                    ctx=Load(),
                                                ),
                                                attr='build_dir',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='setupfile', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='setup_path', ctx=Load()),
                                        attr='split',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='/', kind=None)],
                                    keywords=[],
                                ),
                                slice=UnaryOp(
                                    op=USub(),
                                    operand=Constant(value=1, kind=None),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='setupversion', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='setupfile', ctx=Load()),
                                                    attr='split',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='odoo_setup_', kind=None)],
                                                keywords=[],
                                            ),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='split',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='.exe', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='rsync',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='%s', kind=None),
                                                op=Mod(),
                                                right=Name(id='setup_path', ctx=Load()),
                                            ),
                                            BinOp(
                                                left=Constant(value='%s@127.0.0.1:', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='login',
                                                    ctx=Load(),
                                                ),
                                            ),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='ssh',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='TEMP=/tmp ./%s /S', kind=None),
                                        op=Mod(),
                                        right=Name(id='setupfile', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ssh',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='PGPASSWORD=openpgpwd /cygdrive/c/"Program Files"/"Odoo %s"/PostgreSQL/bin/createdb.exe -e -U openpg mycompany', kind=None),
                                        op=Mod(),
                                        right=Name(id='setupversion', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ssh',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='netsh advfirewall set publicprofile state off', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ssh',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value='/cygdrive/c/"Program Files"/"Odoo {sv}"/python/python.exe \'c:\\Program Files\\Odoo {sv}\\server\\odoo-bin\' -d mycompany -i base --stop-after-init', kind=None),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='sv',
                                                value=Name(id='setupversion', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='_rpc_count_modules', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='port',
                                        value=Constant(value=18069, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Finished testing Windows package', kind=None)],
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
            name='build_exe',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='args', annotation=None, type_comment=None)],
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
                            value=Call(
                                func=Name(id='KVMWinBuildExe', ctx=Load()),
                                args=[Name(id='args', ctx=Load())],
                                keywords=[],
                            ),
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
            name='test_exe',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='args', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                If(
                    test=Attribute(
                        value=Name(id='args', ctx=Load()),
                        attr='test',
                        ctx=Load(),
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='KVMWinTestExe', ctx=Load()),
                                        args=[Name(id='args', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='start',
                                    ctx=Load(),
                                ),
                                args=[],
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
            name='parse_args',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Assign(
                    targets=[Name(id='ap', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='argparse', ctx=Load()),
                            attr='ArgumentParser',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='build_dir', ctx=Store())],
                    value=BinOp(
                        left=Constant(value='%s-%s', kind=None),
                        op=Mod(),
                        right=Tuple(
                            elts=[
                                Name(id='ROOTDIR', ctx=Load()),
                                Name(id='TSTAMP', ctx=Load()),
                            ],
                            ctx=Load(),
                        ),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='log_levels', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='debug', kind=None),
                            Constant(value='info', kind=None),
                            Constant(value='warning', kind=None),
                            Constant(value='error', kind=None),
                            Constant(value='critical', kind=None),
                        ],
                        values=[
                            Attribute(
                                value=Name(id='logging', ctx=Load()),
                                attr='DEBUG',
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id='logging', ctx=Load()),
                                attr='INFO',
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id='logging', ctx=Load()),
                                attr='WARN',
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id='logging', ctx=Load()),
                                attr='ERROR',
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id='logging', ctx=Load()),
                                attr='CRITICAL',
                                ctx=Load(),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='ap', ctx=Load()),
                            attr='add_argument',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='-b', kind=None),
                            Constant(value='--build-dir', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Name(id='build_dir', ctx=Load()),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='build directory (%(default)s)', kind=None),
                            ),
                            keyword(
                                arg='metavar',
                                value=Constant(value='DIR', kind=None),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='ap', ctx=Load()),
                            attr='add_argument',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='-p', kind=None),
                            Constant(value='--pub', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=None, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='pub directory %(default)s', kind=None),
                            ),
                            keyword(
                                arg='metavar',
                                value=Constant(value='DIR', kind=None),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='ap', ctx=Load()),
                            attr='add_argument',
                            ctx=Load(),
                        ),
                        args=[Constant(value='--logging', kind=None)],
                        keywords=[
                            keyword(
                                arg='action',
                                value=Constant(value='store', kind=None),
                            ),
                            keyword(
                                arg='choices',
                                value=Call(
                                    func=Name(id='list', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='log_levels', ctx=Load()),
                                                attr='keys',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='info', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Logging level', kind=None),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='ap', ctx=Load()),
                            attr='add_argument',
                            ctx=Load(),
                        ),
                        args=[Constant(value='--build-deb', kind=None)],
                        keywords=[
                            keyword(
                                arg='action',
                                value=Constant(value='store_true', kind=None),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='ap', ctx=Load()),
                            attr='add_argument',
                            ctx=Load(),
                        ),
                        args=[Constant(value='--build-rpm', kind=None)],
                        keywords=[
                            keyword(
                                arg='action',
                                value=Constant(value='store_true', kind=None),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='ap', ctx=Load()),
                            attr='add_argument',
                            ctx=Load(),
                        ),
                        args=[Constant(value='--build-tgz', kind=None)],
                        keywords=[
                            keyword(
                                arg='action',
                                value=Constant(value='store_true', kind=None),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='ap', ctx=Load()),
                            attr='add_argument',
                            ctx=Load(),
                        ),
                        args=[Constant(value='--build-win', kind=None)],
                        keywords=[
                            keyword(
                                arg='action',
                                value=Constant(value='store_true', kind=None),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='ap', ctx=Load()),
                            attr='add_argument',
                            ctx=Load(),
                        ),
                        args=[Constant(value='--vm-winxp-image', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='/home/odoo/vm/win1036/win10_winpy36.qcow2', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='%(default)s', kind=None),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='ap', ctx=Load()),
                            attr='add_argument',
                            ctx=Load(),
                        ),
                        args=[Constant(value='--vm-winxp-ssh-key', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='/home/odoo/vm/win1036/id_rsa', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='%(default)s', kind=None),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='ap', ctx=Load()),
                            attr='add_argument',
                            ctx=Load(),
                        ),
                        args=[Constant(value='--vm-winxp-login', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='Naresh', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Windows login %(default)s', kind=None),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='ap', ctx=Load()),
                            attr='add_argument',
                            ctx=Load(),
                        ),
                        args=[Constant(value='--vm-winxp-python-version', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='3.7.7', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Windows Python version installed in the VM (default: %(default)s)', kind=None),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='ap', ctx=Load()),
                            attr='add_argument',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='-t', kind=None),
                            Constant(value='--test', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='action',
                                value=Constant(value='store_true', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Test built packages', kind=None),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='ap', ctx=Load()),
                            attr='add_argument',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='-s', kind=None),
                            Constant(value='--sign', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='action',
                                value=Constant(value='store_true', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Sign Debian package / generate Rpm repo', kind=None),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='ap', ctx=Load()),
                            attr='add_argument',
                            ctx=Load(),
                        ),
                        args=[Constant(value='--no-remove', kind=None)],
                        keywords=[
                            keyword(
                                arg='action',
                                value=Constant(value='store_true', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="don't remove build dir", kind=None),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='ap', ctx=Load()),
                            attr='add_argument',
                            ctx=Load(),
                        ),
                        args=[Constant(value='--blacklist', kind=None)],
                        keywords=[
                            keyword(
                                arg='nargs',
                                value=Constant(value='*', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Modules to blacklist in package', kind=None),
                            ),
                        ],
                    ),
                ),
                Assign(
                    targets=[Name(id='parsed_args', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='ap', ctx=Load()),
                            attr='parse_args',
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
                            value=Name(id='logging', ctx=Load()),
                            attr='basicConfig',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='format',
                                value=Constant(value='%(asctime)s %(levelname)s: %(message)s', kind=None),
                            ),
                            keyword(
                                arg='datefmt',
                                value=Constant(value='%Y-%m-%d %I:%M:%S', kind=None),
                            ),
                            keyword(
                                arg='level',
                                value=Subscript(
                                    value=Name(id='log_levels', ctx=Load()),
                                    slice=Attribute(
                                        value=Name(id='parsed_args', ctx=Load()),
                                        attr='logging',
                                        ctx=Load(),
                                    ),
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                ),
                Assign(
                    targets=[
                        Attribute(
                            value=Name(id='parsed_args', ctx=Load()),
                            attr='odoo_dir',
                            ctx=Store(),
                        ),
                    ],
                    value=Name(id='ROOTDIR', ctx=Load()),
                    type_comment=None,
                ),
                Return(
                    value=Name(id='parsed_args', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='main',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='args', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Try(
                    body=[
                        If(
                            test=Attribute(
                                value=Name(id='args', ctx=Load()),
                                attr='build_tgz',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='_prepare_build_dir', ctx=Load()),
                                        args=[Name(id='args', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='docker_tgz', ctx=Store())],
                                    value=Call(
                                        func=Name(id='DockerTgz', ctx=Load()),
                                        args=[Name(id='args', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='docker_tgz', ctx=Load()),
                                            attr='build',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='docker_tgz', ctx=Load()),
                                                    attr='start_test',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='published_files', ctx=Store())],
                                            value=Call(
                                                func=Name(id='publish', ctx=Load()),
                                                args=[
                                                    Name(id='args', ctx=Load()),
                                                    Constant(value='tgz', kind=None),
                                                    List(
                                                        elts=[
                                                            Constant(value='tar.gz', kind=None),
                                                            Constant(value='zip', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
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
                                                            value=Name(id='logging', ctx=Load()),
                                                            attr='error',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value="Won't publish the tgz release.\n Exception: %s", kind=None),
                                                                op=Mod(),
                                                                right=Call(
                                                                    func=Name(id='str', ctx=Load()),
                                                                    args=[Name(id='e', ctx=Load())],
                                                                    keywords=[],
                                                                ),
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
                        If(
                            test=Attribute(
                                value=Name(id='args', ctx=Load()),
                                attr='build_rpm',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='_prepare_build_dir', ctx=Load()),
                                        args=[Name(id='args', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='docker_rpm', ctx=Store())],
                                    value=Call(
                                        func=Name(id='DockerRpm', ctx=Load()),
                                        args=[Name(id='args', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='docker_rpm', ctx=Load()),
                                            attr='build',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='docker_rpm', ctx=Load()),
                                                    attr='start_test',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='published_files', ctx=Store())],
                                            value=Call(
                                                func=Name(id='publish', ctx=Load()),
                                                args=[
                                                    Name(id='args', ctx=Load()),
                                                    Constant(value='rpm', kind=None),
                                                    List(
                                                        elts=[Constant(value='rpm', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='sign',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='logging', ctx=Load()),
                                                            attr='info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='Signing rpm package', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='rpm_sign', ctx=Load()),
                                                        args=[
                                                            Name(id='args', ctx=Load()),
                                                            Subscript(
                                                                value=Name(id='published_files', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='logging', ctx=Load()),
                                                            attr='info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='Generate rpm repo', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='docker_rpm', ctx=Load()),
                                                            attr='gen_rpm_repo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='args', ctx=Load()),
                                                            Subscript(
                                                                value=Name(id='published_files', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
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
                                                            value=Name(id='logging', ctx=Load()),
                                                            attr='error',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value="Won't publish the rpm release.\n Exception: %s", kind=None),
                                                                op=Mod(),
                                                                right=Call(
                                                                    func=Name(id='str', ctx=Load()),
                                                                    args=[Name(id='e', ctx=Load())],
                                                                    keywords=[],
                                                                ),
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
                        If(
                            test=Attribute(
                                value=Name(id='args', ctx=Load()),
                                attr='build_deb',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='_prepare_build_dir', ctx=Load()),
                                        args=[Name(id='args', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='move_addons',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='docker_deb', ctx=Store())],
                                    value=Call(
                                        func=Name(id='DockerDeb', ctx=Load()),
                                        args=[Name(id='args', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='docker_deb', ctx=Load()),
                                            attr='build',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='docker_deb', ctx=Load()),
                                                    attr='start_test',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='published_files', ctx=Store())],
                                            value=Call(
                                                func=Name(id='publish', ctx=Load()),
                                                args=[
                                                    Name(id='args', ctx=Load()),
                                                    Constant(value='deb', kind=None),
                                                    List(
                                                        elts=[
                                                            Constant(value='deb', kind=None),
                                                            Constant(value='dsc', kind=None),
                                                            Constant(value='changes', kind=None),
                                                            Constant(value='tar.xz', kind=None),
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
                                                func=Name(id='gen_deb_package', ctx=Load()),
                                                args=[
                                                    Name(id='args', ctx=Load()),
                                                    Name(id='published_files', ctx=Load()),
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
                                                            value=Name(id='logging', ctx=Load()),
                                                            attr='error',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value="Won't publish the deb release.\n Exception: %s", kind=None),
                                                                op=Mod(),
                                                                right=Call(
                                                                    func=Name(id='str', ctx=Load()),
                                                                    args=[Name(id='e', ctx=Load())],
                                                                    keywords=[],
                                                                ),
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
                        If(
                            test=Attribute(
                                value=Name(id='args', ctx=Load()),
                                attr='build_win',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='_prepare_build_dir', ctx=Load()),
                                        args=[Name(id='args', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='win32',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='build_exe', ctx=Load()),
                                        args=[Name(id='args', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='test_exe', ctx=Load()),
                                                args=[Name(id='args', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='published_files', ctx=Store())],
                                            value=Call(
                                                func=Name(id='publish', ctx=Load()),
                                                args=[
                                                    Name(id='args', ctx=Load()),
                                                    Constant(value='windows', kind=None),
                                                    List(
                                                        elts=[Constant(value='exe', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
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
                                                            value=Name(id='logging', ctx=Load()),
                                                            attr='error',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value="Won't publish the exe release.\n Exception: %s", kind=None),
                                                                op=Mod(),
                                                                right=Call(
                                                                    func=Name(id='str', ctx=Load()),
                                                                    args=[Name(id='e', ctx=Load())],
                                                                    keywords=[],
                                                                ),
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
                    handlers=[
                        ExceptHandler(
                            type=Name(id='Exception', ctx=Load()),
                            name='e',
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='logging', ctx=Load()),
                                            attr='error',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value='Something bad happened ! : {}', kind=None),
                                                    attr='format',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='e', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='traceback', ctx=Load()),
                                            attr='print_exc',
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
                    finalbody=[
                        If(
                            test=Attribute(
                                value=Name(id='args', ctx=Load()),
                                attr='no_remove',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='logging', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value='Build dir "{}" not removed', kind=None),
                                                    attr='format',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='args', ctx=Load()),
                                                        attr='build_dir',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
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
                                        args=[
                                            Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='build_dir',
                                                ctx=Load(),
                                            ),
                                        ],
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
                                                args=[
                                                    Attribute(
                                                        value=Name(id='args', ctx=Load()),
                                                        attr='build_dir',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='logging', ctx=Load()),
                                                    attr='info',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='Build dir %s removed', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='args', ctx=Load()),
                                                            attr='build_dir',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
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
        If(
            test=Compare(
                left=Name(id='__name__', ctx=Load()),
                ops=[Eq()],
                comparators=[Constant(value='__main__', kind=None)],
            ),
            body=[
                Assign(
                    targets=[Name(id='args', ctx=Store())],
                    value=Call(
                        func=Name(id='parse_args', ctx=Load()),
                        args=[],
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
                        args=[
                            Attribute(
                                value=Name(id='args', ctx=Load()),
                                attr='build_dir',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='error',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Build dir "%s" already exists.', kind=None),
                                    Attribute(
                                        value=Name(id='args', ctx=Load()),
                                        attr='build_dir',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sys', ctx=Load()),
                                    attr='exit',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=1, kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Expr(
                    value=Call(
                        func=Name(id='main', ctx=Load()),
                        args=[Name(id='args', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            orelse=[],
        ),
    ],
    type_ignores=[],
)
