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
            names=[alias(name='sys', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        Expr(
            value=Call(
                func=Attribute(
                    value=Attribute(
                        value=Name(id='sys', ctx=Load()),
                        attr='path',
                        ctx=Load(),
                    ),
                    attr='append',
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
                            attr='abspath',
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
                                    Name(id='__file__', ctx=Load()),
                                    Constant(value='../../../', kind=None),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ],
                keywords=[],
            ),
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='topological_sort', asname=None),
                alias(name='unique', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.netsvc',
            names=[alias(name='init_logger', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='standalone_tests', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='odoo.tests.loader', asname=None)],
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Constant(value='odoo.tests.test_module_operations', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='BLACKLIST', ctx=Store())],
            value=Set(
                elts=[
                    Constant(value='auth_ldap', kind=None),
                    Constant(value='document_ftp', kind=None),
                    Constant(value='website_instantclick', kind=None),
                    Constant(value='pad', kind=None),
                    Constant(value='pad_project', kind=None),
                    Constant(value='note_pad', kind=None),
                    Constant(value='pos_cache', kind=None),
                    Constant(value='pos_blackbox_be', kind=None),
                    Constant(value='payment_test', kind=None),
                ],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='IGNORE', ctx=Store())],
            value=Tuple(
                elts=[
                    Constant(value='hw_', kind=None),
                    Constant(value='theme_', kind=None),
                    Constant(value='l10n_', kind=None),
                    Constant(value='test_', kind=None),
                    Constant(value='payment_', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='install',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='db_name', annotation=None, type_comment=None),
                    arg(arg='module_id', annotation=None, type_comment=None),
                    arg(arg='module_name', annotation=None, type_comment=None),
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
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='registry',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='db_name', ctx=Load())],
                                        keywords=[],
                                    ),
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
                                    Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='SUPERUSER_ID',
                                        ctx=Load(),
                                    ),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='module', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='env', ctx=Load()),
                                        slice=Constant(value='ir.module.module', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='module_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='module', ctx=Load()),
                                    attr='button_immediate_install',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                            Constant(value='%s installed', kind=None),
                            Name(id='module_name', ctx=Load()),
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
            name='uninstall',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='db_name', annotation=None, type_comment=None),
                    arg(arg='module_id', annotation=None, type_comment=None),
                    arg(arg='module_name', annotation=None, type_comment=None),
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
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='registry',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='db_name', ctx=Load())],
                                        keywords=[],
                                    ),
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
                                    Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='SUPERUSER_ID',
                                        ctx=Load(),
                                    ),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='module', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='env', ctx=Load()),
                                        slice=Constant(value='ir.module.module', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='module_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='module', ctx=Load()),
                                    attr='button_immediate_uninstall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                            Constant(value='%s uninstalled', kind=None),
                            Name(id='module_name', ctx=Load()),
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
            name='cycle',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='db_name', annotation=None, type_comment=None),
                    arg(arg='module_id', annotation=None, type_comment=None),
                    arg(arg='module_name', annotation=None, type_comment=None),
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
                        func=Name(id='install', ctx=Load()),
                        args=[
                            Name(id='db_name', ctx=Load()),
                            Name(id='module_id', ctx=Load()),
                            Name(id='module_name', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Name(id='uninstall', ctx=Load()),
                        args=[
                            Name(id='db_name', ctx=Load()),
                            Name(id='module_id', ctx=Load()),
                            Name(id='module_name', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Name(id='install', ctx=Load()),
                        args=[
                            Name(id='db_name', ctx=Load()),
                            Name(id='module_id', ctx=Load()),
                            Name(id='module_name', ctx=Load()),
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
            name='parse_args',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Assign(
                    targets=[Name(id='parser', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='argparse', ctx=Load()),
                            attr='ArgumentParser',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='description',
                                value=Constant(value='Script for testing the install / uninstall / reinstall cycle of Odoo modules', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='parser', ctx=Load()),
                            attr='add_argument',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='--database', kind=None),
                            Constant(value='-d', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='type',
                                value=Name(id='str', ctx=Load()),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="The database to test (note: must have only 'base' installed)", kind=None),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='parser', ctx=Load()),
                            attr='add_argument',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='--data-dir', kind=None),
                            Constant(value='-D', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='dest',
                                value=Constant(value='data_dir', kind=None),
                            ),
                            keyword(
                                arg='type',
                                value=Name(id='str', ctx=Load()),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Directory where to store Odoo data', kind=None),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='parser', ctx=Load()),
                            attr='add_argument',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='--skip', kind=None),
                            Constant(value='-s', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='type',
                                value=Name(id='str', ctx=Load()),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Comma-separated list of modules to skip (they will only be installed)', kind=None),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='parser', ctx=Load()),
                            attr='add_argument',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='--resume-at', kind=None),
                            Constant(value='-r', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='type',
                                value=Name(id='str', ctx=Load()),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Skip modules (only install) up to the specified one in topological order', kind=None),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='parser', ctx=Load()),
                            attr='add_argument',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='--addons-path', kind=None),
                            Constant(value='-p', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='type',
                                value=Name(id='str', ctx=Load()),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Comma-separated list of paths to directories containing extra Odoo modules', kind=None),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='parser', ctx=Load()),
                            attr='add_argument',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='--uninstall', kind=None),
                            Constant(value='-U', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='type',
                                value=Name(id='str', ctx=Load()),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Comma-separated list of modules to uninstall/reinstall', kind=None),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='parser', ctx=Load()),
                            attr='add_argument',
                            ctx=Load(),
                        ),
                        args=[Constant(value='--standalone', kind=None)],
                        keywords=[
                            keyword(
                                arg='type',
                                value=Name(id='str', ctx=Load()),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="Launch standalone scripts tagged with @standalone. Accepts a list of module names or tags separated by commas. 'all' will run all available scripts.", kind=None),
                            ),
                        ],
                    ),
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='parser', ctx=Load()),
                            attr='parse_args',
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
            name='test_full',
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
                    value=Constant(value=' Test full install/uninstall/reinstall cycle for all modules ', kind=None),
                ),
                With(
                    items=[
                        withitem(
                            context_expr=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='registry',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='database',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
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
                                    Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='SUPERUSER_ID',
                                        ctx=Load(),
                                    ),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='valid',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='module', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=UnaryOp(
                                        op=Not(),
                                        operand=BoolOp(
                                            op=Or(),
                                            values=[
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='module', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[In()],
                                                    comparators=[Name(id='BLACKLIST', ctx=Load())],
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='module', ctx=Load()),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                        attr='startswith',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='IGNORE', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='module', ctx=Load()),
                                                        attr='state',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[In()],
                                                    comparators=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='installed', kind=None),
                                                                Constant(value='uninstallable', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='modules', ctx=Store())],
                            value=Call(
                                func=Attribute(
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
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[Name(id='valid', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='modules', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='modules', ctx=Load()),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='topological_sort', ctx=Load()),
                                        args=[
                                            DictComp(
                                                key=Attribute(
                                                    value=Name(id='module', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='module', ctx=Load()),
                                                            attr='dependencies_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='depend_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='module', ctx=Store()),
                                                        iter=Name(id='modules', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
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
                            targets=[Name(id='modules_todo', ctx=Store())],
                            value=ListComp(
                                elt=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='module', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='module', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='module', ctx=Store()),
                                        iter=Name(id='modules', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='resume', ctx=Store())],
                    value=Attribute(
                        value=Name(id='args', ctx=Load()),
                        attr='resume_at',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='skip', ctx=Store())],
                    value=IfExp(
                        test=Attribute(
                            value=Name(id='args', ctx=Load()),
                            attr='skip',
                            ctx=Load(),
                        ),
                        body=Call(
                            func=Name(id='set', ctx=Load()),
                            args=[
                                Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='args', ctx=Load()),
                                            attr='skip',
                                            ctx=Load(),
                                        ),
                                        attr='split',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value=',', kind=None)],
                                    keywords=[],
                                ),
                            ],
                            keywords=[],
                        ),
                        orelse=Call(
                            func=Name(id='set', ctx=Load()),
                            args=[],
                            keywords=[],
                        ),
                    ),
                    type_comment=None,
                ),
                For(
                    target=Tuple(
                        elts=[
                            Name(id='module_id', ctx=Store()),
                            Name(id='module_name', ctx=Store()),
                        ],
                        ctx=Store(),
                    ),
                    iter=Name(id='modules_todo', ctx=Load()),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='module_name', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Name(id='resume', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='resume', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='resume', ctx=Load()),
                                    Compare(
                                        left=Name(id='module_name', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='skip', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='install', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='database',
                                                ctx=Load(),
                                            ),
                                            Name(id='module_id', ctx=Load()),
                                            Name(id='module_name', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Name(id='cycle', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='database',
                                                ctx=Load(),
                                            ),
                                            Name(id='module_id', ctx=Load()),
                                            Name(id='module_name', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
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
        FunctionDef(
            name='test_uninstall',
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
                    value=Constant(value=' Tries to uninstall/reinstall one ore more modules', kind=None),
                ),
                Assign(
                    targets=[Name(id='domain', ctx=Store())],
                    value=List(
                        elts=[
                            Tuple(
                                elts=[
                                    Constant(value='name', kind=None),
                                    Constant(value='in', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='uninstall',
                                                ctx=Load(),
                                            ),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=',', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
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
                    type_comment=None,
                ),
                With(
                    items=[
                        withitem(
                            context_expr=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='registry',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='database',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
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
                                    Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='SUPERUSER_ID',
                                        ctx=Load(),
                                    ),
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
                                    value=Subscript(
                                        value=Name(id='env', ctx=Load()),
                                        slice=Constant(value='ir.module.module', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='modules_todo', ctx=Store())],
                            value=ListComp(
                                elt=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='module', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='module', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='module', ctx=Store()),
                                        iter=Name(id='modules', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    type_comment=None,
                ),
                For(
                    target=Tuple(
                        elts=[
                            Name(id='module_id', ctx=Store()),
                            Name(id='module_name', ctx=Store()),
                        ],
                        ctx=Store(),
                    ),
                    iter=Name(id='modules_todo', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='uninstall', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='args', ctx=Load()),
                                        attr='database',
                                        ctx=Load(),
                                    ),
                                    Name(id='module_id', ctx=Load()),
                                    Name(id='module_name', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='install', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='args', ctx=Load()),
                                        attr='database',
                                        ctx=Load(),
                                    ),
                                    Name(id='module_id', ctx=Load()),
                                    Name(id='module_name', ctx=Load()),
                                ],
                                keywords=[],
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
        FunctionDef(
            name='test_scripts',
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
                    value=Constant(value=' Tries to launch standalone scripts tagged with @post_testing ', kind=None),
                ),
                Assign(
                    targets=[Name(id='registry', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='registry',
                            ctx=Load(),
                        ),
                        args=[
                            Attribute(
                                value=Name(id='args', ctx=Load()),
                                attr='database',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='module_name', ctx=Store()),
                    iter=Attribute(
                        value=Name(id='registry', ctx=Load()),
                        attr='_init_modules',
                        ctx=Load(),
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='tests',
                                            ctx=Load(),
                                        ),
                                        attr='loader',
                                        ctx=Load(),
                                    ),
                                    attr='get_test_modules',
                                    ctx=Load(),
                                ),
                                args=[Name(id='module_name', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='funcs', ctx=Store())],
                    value=Call(
                        func=Name(id='list', ctx=Load()),
                        args=[
                            Call(
                                func=Name(id='unique', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Name(id='func', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='tag', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='args', ctx=Load()),
                                                            attr='standalone',
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
                                            comprehension(
                                                target=Name(id='func', ctx=Store()),
                                                iter=Subscript(
                                                    value=Name(id='standalone_tests', ctx=Load()),
                                                    slice=Name(id='tag', ctx=Load()),
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
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
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
                For(
                    target=Tuple(
                        elts=[
                            Name(id='index', ctx=Store()),
                            Name(id='func', ctx=Store()),
                        ],
                        ctx=Store(),
                    ),
                    iter=Call(
                        func=Name(id='enumerate', ctx=Load()),
                        args=[Name(id='funcs', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='start',
                                value=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    body=[
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='odoo', ctx=Load()),
                                                    attr='registry',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='args', ctx=Load()),
                                                        attr='database',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
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
                                            Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='SUPERUSER_ID',
                                                ctx=Load(),
                                            ),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
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
                                            Constant(value='Executing standalone script: %s (%d / %d)', kind=None),
                                            Attribute(
                                                value=Name(id='func', ctx=Load()),
                                                attr='__name__',
                                                ctx=Load(),
                                            ),
                                            Name(id='index', ctx=Load()),
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='funcs', ctx=Load())],
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
                                                func=Name(id='func', ctx=Load()),
                                                args=[Name(id='env', ctx=Load())],
                                                keywords=[],
                                            ),
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
                                                            attr='error',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Standalone script %s failed', kind=None),
                                                            Attribute(
                                                                value=Name(id='func', ctx=Load()),
                                                                attr='__name__',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='exc_info',
                                                                value=Constant(value=True, kind=None),
                                                            ),
                                                        ],
                                                    ),
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
                    ],
                    orelse=[],
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
                            BinOp(
                                left=Constant(value='%d standalone scripts executed in %.2fs', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='funcs', ctx=Load())],
                                            keywords=[],
                                        ),
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
                                    ctx=Load(),
                                ),
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
                    test=Attribute(
                        value=Name(id='args', ctx=Load()),
                        attr='addons_path',
                        ctx=Load(),
                    ),
                    body=[
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
                                    slice=Constant(value='addons_path', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=',', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='addons_path',
                                                ctx=Load(),
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
                                                slice=Constant(value='addons_path', kind=None),
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
                            test=Attribute(
                                value=Name(id='args', ctx=Load()),
                                attr='data_dir',
                                ctx=Load(),
                            ),
                            body=[
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
                                            slice=Constant(value='data_dir', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='args', ctx=Load()),
                                        attr='data_dir',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='modules',
                                            ctx=Load(),
                                        ),
                                        attr='module',
                                        ctx=Load(),
                                    ),
                                    attr='initialize_sys_path',
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
                        func=Name(id='init_logger', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='getLogger',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='odoo.modules.loading', kind=None)],
                                keywords=[],
                            ),
                            attr='setLevel',
                            ctx=Load(),
                        ),
                        args=[
                            Attribute(
                                value=Name(id='logging', ctx=Load()),
                                attr='CRITICAL',
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
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='getLogger',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='odoo.sql_db', kind=None)],
                                keywords=[],
                            ),
                            attr='setLevel',
                            ctx=Load(),
                        ),
                        args=[
                            Attribute(
                                value=Name(id='logging', ctx=Load()),
                                attr='CRITICAL',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                If(
                    test=Attribute(
                        value=Name(id='args', ctx=Load()),
                        attr='uninstall',
                        ctx=Load(),
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='test_uninstall', ctx=Load()),
                                args=[Name(id='args', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[
                        If(
                            test=Attribute(
                                value=Name(id='args', ctx=Load()),
                                attr='standalone',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='test_scripts', ctx=Load()),
                                        args=[Name(id='args', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Name(id='test_full', ctx=Load()),
                                        args=[Name(id='args', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                ),
            ],
            orelse=[],
        ),
    ],
    type_ignores=[],
)
