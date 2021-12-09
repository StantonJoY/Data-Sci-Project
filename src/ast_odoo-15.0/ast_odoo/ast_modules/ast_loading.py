Module(
    body=[
        Expr(
            value=Constant(value=' Modules (also called addons) management.\n\n', kind=None),
        ),
        Import(
            names=[alias(name='itertools', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='sys', asname=None)],
        ),
        Import(
            names=[alias(name='threading', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        Import(
            names=[alias(name='odoo.modules.db', asname=None)],
        ),
        Import(
            names=[alias(name='odoo.modules.graph', asname=None)],
        ),
        Import(
            names=[alias(name='odoo.modules.migration', asname=None)],
        ),
        Import(
            names=[alias(name='odoo.modules.registry', asname=None)],
        ),
        ImportFrom(
            module=None,
            names=[
                alias(name='SUPERUSER_ID', asname=None),
                alias(name='api', asname=None),
                alias(name='tools', asname=None),
            ],
            level=2,
        ),
        ImportFrom(
            module='module',
            names=[
                alias(name='adapt_version', asname=None),
                alias(name='initialize_sys_path', asname=None),
                alias(name='load_openerp_module', asname=None),
            ],
            level=1,
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
        Assign(
            targets=[Name(id='_test_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Constant(value='odoo.tests', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='load_data',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='idref', annotation=None, type_comment=None),
                    arg(arg='mode', annotation=None, type_comment=None),
                    arg(arg='kind', annotation=None, type_comment=None),
                    arg(arg='package', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n\n    kind: data, demo, test, init_xml, update_xml, demo_xml.\n\n    noupdate is False, unless it is demo data or it is csv data in\n    init mode.\n\n    :returns: Whether a file was loaded\n    :rtype: bool\n    ', kind=None),
                ),
                FunctionDef(
                    name='_get_files_of_kind',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='kind', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='kind', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='demo', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='kind', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Constant(value='demo_xml', kind=None),
                                            Constant(value='demo', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='kind', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='data', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='kind', ctx=Store())],
                                            value=List(
                                                elts=[
                                                    Constant(value='init_xml', kind=None),
                                                    Constant(value='update_xml', kind=None),
                                                    Constant(value='data', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='kind', ctx=Load()),
                                    Name(id='str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='kind', ctx=Store())],
                                    value=List(
                                        elts=[Name(id='kind', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='files', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='k', ctx=Store()),
                            iter=Name(id='kind', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='f', ctx=Store()),
                                    iter=Subscript(
                                        value=Attribute(
                                            value=Name(id='package', ctx=Load()),
                                            attr='data',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='k', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='files', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='f', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='k', ctx=Load()),
                                                            attr='endswith',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='_xml', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=BoolOp(
                                                            op=And(),
                                                            values=[
                                                                Compare(
                                                                    left=Name(id='k', ctx=Load()),
                                                                    ops=[Eq()],
                                                                    comparators=[Constant(value='init_xml', kind=None)],
                                                                ),
                                                                UnaryOp(
                                                                    op=Not(),
                                                                    operand=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='f', ctx=Load()),
                                                                            attr='endswith',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='.xml', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='correct_key', ctx=Store())],
                                                    value=IfExp(
                                                        test=Call(
                                                            func=Attribute(
                                                                value=Name(id='k', ctx=Load()),
                                                                attr='count',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='demo', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        body=Constant(value='demo', kind=None),
                                                        orelse=Constant(value='data', kind=None),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value="module %s: key '%s' is deprecated in favor of '%s' for file '%s'.", kind=None),
                                                            Attribute(
                                                                value=Name(id='package', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='k', ctx=Load()),
                                                            Name(id='correct_key', ctx=Load()),
                                                            Name(id='f', ctx=Load()),
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='files', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='filename', ctx=Store())],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
                Try(
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='kind', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='demo', kind=None),
                                            Constant(value='test', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='threading', ctx=Load()),
                                                    attr='currentThread',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='testing',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='filename', ctx=Store()),
                            iter=Call(
                                func=Name(id='_get_files_of_kind', ctx=Load()),
                                args=[Name(id='kind', ctx=Load())],
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
                                            Constant(value='loading %s/%s', kind=None),
                                            Attribute(
                                                value=Name(id='package', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Name(id='filename', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='noupdate', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Name(id='kind', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='demo', kind=None),
                                                            Constant(value='demo_xml', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='filename', ctx=Load()),
                                                            attr='endswith',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='.csv', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Compare(
                                                        left=Name(id='kind', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='init', kind=None),
                                                                    Constant(value='init_xml', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='noupdate', ctx=Store())],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='convert_file',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='cr', ctx=Load()),
                                            Attribute(
                                                value=Name(id='package', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Name(id='filename', ctx=Load()),
                                            Name(id='idref', ctx=Load()),
                                            Name(id='mode', ctx=Load()),
                                            Name(id='noupdate', ctx=Load()),
                                            Name(id='kind', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    handlers=[],
                    orelse=[],
                    finalbody=[
                        If(
                            test=Compare(
                                left=Name(id='kind', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='demo', kind=None),
                                            Constant(value='test', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='threading', ctx=Load()),
                                                    attr='currentThread',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='testing',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                ),
                Return(
                    value=Call(
                        func=Name(id='bool', ctx=Load()),
                        args=[Name(id='filename', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='load_demo',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='package', annotation=None, type_comment=None),
                    arg(arg='idref', annotation=None, type_comment=None),
                    arg(arg='mode', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Loads demo data for the specified package.\n    ', kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Call(
                            func=Attribute(
                                value=Name(id='package', ctx=Load()),
                                attr='should_have_demo',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                    ),
                    body=[
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Try(
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Module %s: loading demo', kind=None),
                                    Attribute(
                                        value=Name(id='package', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='savepoint',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='flush',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='load_data', ctx=Load()),
                                        args=[
                                            Name(id='cr', ctx=Load()),
                                            Name(id='idref', ctx=Load()),
                                            Name(id='mode', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='kind',
                                                value=Constant(value='demo', kind=None),
                                            ),
                                            keyword(
                                                arg='package',
                                                value=Name(id='package', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
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
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Module %s demo data failed to install, installed without demo data', kind=None),
                                            Attribute(
                                                value=Name(id='package', ctx=Load()),
                                                attr='name',
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
                                Assign(
                                    targets=[Name(id='env', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='api', ctx=Load()),
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
                                Assign(
                                    targets=[Name(id='todo', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='env', ctx=Load()),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='base.demo_failure_todo', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='raise_if_not_found',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='Failure', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='env', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='ir.demo_failure', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='todo', ctx=Load()),
                                            Compare(
                                                left=Name(id='Failure', ctx=Load()),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='todo', ctx=Load()),
                                                    attr='state',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='open', kind=None),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Failure', ctx=Load()),
                                                    attr='create',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='module_id', kind=None),
                                                            Constant(value='error', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='package', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[Name(id='e', ctx=Load())],
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
                                    value=Constant(value=False, kind=None),
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
            name='force_demo',
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
                Expr(
                    value=Constant(value='\n    Forces the `demo` flag on all modules, and installs demo data for all installed modules.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='graph', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='modules',
                                    ctx=Load(),
                                ),
                                attr='graph',
                                ctx=Load(),
                            ),
                            attr='Graph',
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
                            value=Name(id='cr', ctx=Load()),
                            attr='execute',
                            ctx=Load(),
                        ),
                        args=[Constant(value='UPDATE ir_module_module SET demo=True', kind=None)],
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
                        args=[Constant(value="SELECT name FROM ir_module_module WHERE state IN ('installed', 'to upgrade', 'to remove')", kind=None)],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='module_list', ctx=Store())],
                    value=ListComp(
                        elt=Name(id='name', ctx=Load()),
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
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='graph', ctx=Load()),
                            attr='add_modules',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='cr', ctx=Load()),
                            Name(id='module_list', ctx=Load()),
                            List(
                                elts=[Constant(value='demo', kind=None)],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                For(
                    target=Name(id='package', ctx=Store()),
                    iter=Name(id='graph', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='load_demo', ctx=Load()),
                                args=[
                                    Name(id='cr', ctx=Load()),
                                    Name(id='package', ctx=Load()),
                                    Dict(keys=[], values=[]),
                                    Constant(value='init', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='env', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='api', ctx=Load()),
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
                                slice=Constant(value='ir.module.module', kind=None),
                                ctx=Load(),
                            ),
                            attr='invalidate_cache',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[Constant(value='demo', kind=None)],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Subscript(
                                value=Name(id='env', ctx=Load()),
                                slice=Constant(value='res.groups', kind=None),
                                ctx=Load(),
                            ),
                            attr='_update_user_groups_view',
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
            name='load_module_graph',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='graph', annotation=None, type_comment=None),
                    arg(arg='status', annotation=None, type_comment=None),
                    arg(arg='perform_checks', annotation=None, type_comment=None),
                    arg(arg='skip_modules', annotation=None, type_comment=None),
                    arg(arg='report', annotation=None, type_comment=None),
                    arg(arg='models_to_check', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=True, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value='Migrates+Updates or Installs all module nodes from ``graph``\n       :param graph: graph of module nodes to load\n       :param status: deprecated parameter, unused, left to avoid changing signature in 8.0\n       :param perform_checks: whether module descriptors should be checked for validity (prints warnings\n                              for same cases)\n       :param skip_modules: optional list of module names (packages) which have previously been loaded and can be skipped\n       :return: list of modules that were installed or updated\n    ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Name(id='models_to_check', ctx=Load()),
                        ops=[Is()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='models_to_check', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='processed_modules', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='loaded_modules', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
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
                                value=Name(id='cr', ctx=Load()),
                                attr='dbname',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='migrations', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='modules',
                                    ctx=Load(),
                                ),
                                attr='migration',
                                ctx=Load(),
                            ),
                            attr='MigrationManager',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='cr', ctx=Load()),
                            Name(id='graph', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_count', ctx=Store())],
                    value=Call(
                        func=Name(id='len', ctx=Load()),
                        args=[Name(id='graph', ctx=Load())],
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
                            Constant(value='loading %d modules...', kind=None),
                            Name(id='module_count', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='t0', ctx=Store())],
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
                Assign(
                    targets=[Name(id='loading_extra_query_count', ctx=Store())],
                    value=Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='sql_db',
                            ctx=Load(),
                        ),
                        attr='sql_counter',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='loading_cursor_query_count', ctx=Store())],
                    value=Attribute(
                        value=Name(id='cr', ctx=Load()),
                        attr='sql_log_count',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='models_updated', ctx=Store())],
                    value=Call(
                        func=Name(id='set', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Tuple(
                        elts=[
                            Name(id='index', ctx=Store()),
                            Name(id='package', ctx=Store()),
                        ],
                        ctx=Store(),
                    ),
                    iter=Call(
                        func=Name(id='enumerate', ctx=Load()),
                        args=[
                            Name(id='graph', ctx=Load()),
                            Constant(value=1, kind=None),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='module_name', ctx=Store())],
                            value=Attribute(
                                value=Name(id='package', ctx=Load()),
                                attr='name',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='module_id', ctx=Store())],
                            value=Attribute(
                                value=Name(id='package', ctx=Load()),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='skip_modules', ctx=Load()),
                                    Compare(
                                        left=Name(id='module_name', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='skip_modules', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[Continue()],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='module_t0', ctx=Store())],
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
                        Assign(
                            targets=[Name(id='module_cursor_query_count', ctx=Store())],
                            value=Attribute(
                                value=Name(id='cr', ctx=Load()),
                                attr='sql_log_count',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='module_extra_query_count', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='sql_db',
                                    ctx=Load(),
                                ),
                                attr='sql_counter',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='needs_update', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Name(id='hasattr', ctx=Load()),
                                        args=[
                                            Name(id='package', ctx=Load()),
                                            Constant(value='init', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='hasattr', ctx=Load()),
                                        args=[
                                            Name(id='package', ctx=Load()),
                                            Constant(value='update', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='package', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='to install', kind=None),
                                                    Constant(value='to upgrade', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='module_log_level', ctx=Store())],
                            value=Attribute(
                                value=Name(id='logging', ctx=Load()),
                                attr='DEBUG',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='needs_update', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='module_log_level', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='logging', ctx=Load()),
                                        attr='INFO',
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
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='log',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='module_log_level', ctx=Load()),
                                    Constant(value='Loading module %s (%d/%d)', kind=None),
                                    Name(id='module_name', ctx=Load()),
                                    Name(id='index', ctx=Load()),
                                    Name(id='module_count', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='needs_update', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='package', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='base', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='registry', ctx=Load()),
                                                    attr='setup_models',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='cr', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='migrations', ctx=Load()),
                                            attr='migrate_module',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='package', ctx=Load()),
                                            Constant(value='pre', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='package', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='base', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='env', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='api', ctx=Load()),
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
                                                        slice=Constant(value='base', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='flush',
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
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='load_openerp_module', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='package', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='new_install', ctx=Store())],
                            value=Compare(
                                left=Attribute(
                                    value=Name(id='package', ctx=Load()),
                                    attr='state',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='to install', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='new_install', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='py_module', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='sys', ctx=Load()),
                                            attr='modules',
                                            ctx=Load(),
                                        ),
                                        slice=BinOp(
                                            left=Constant(value='odoo.addons.%s', kind=None),
                                            op=Mod(),
                                            right=Tuple(
                                                elts=[Name(id='module_name', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='pre_init', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='package', ctx=Load()),
                                                attr='info',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='pre_init_hook', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='pre_init', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Call(
                                                    func=Name(id='getattr', ctx=Load()),
                                                    args=[
                                                        Name(id='py_module', ctx=Load()),
                                                        Name(id='pre_init', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                                args=[Name(id='cr', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='model_names', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='registry', ctx=Load()),
                                    attr='load',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='cr', ctx=Load()),
                                    Name(id='package', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mode', ctx=Store())],
                            value=Constant(value='update', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Name(id='hasattr', ctx=Load()),
                                        args=[
                                            Name(id='package', ctx=Load()),
                                            Constant(value='init', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='package', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='to install', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='mode', ctx=Store())],
                                    value=Constant(value='init', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='loaded_modules', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='package', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='needs_update', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='models_updated', ctx=Store()),
                                    op=BitOr(),
                                    value=Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[Name(id='model_names', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                AugAssign(
                                    target=Name(id='models_to_check', ctx=Store()),
                                    op=Sub(),
                                    value=Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[Name(id='model_names', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='registry', ctx=Load()),
                                            attr='setup_models',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='cr', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='registry', ctx=Load()),
                                            attr='init_models',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='cr', ctx=Load()),
                                            Name(id='model_names', ctx=Load()),
                                            Dict(
                                                keys=[Constant(value='module', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='package', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Name(id='new_install', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='package', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='to remove', kind=None)],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='models_to_check', ctx=Store()),
                                            op=BitOr(),
                                            value=BinOp(
                                                left=Call(
                                                    func=Name(id='set', ctx=Load()),
                                                    args=[Name(id='model_names', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                op=BitAnd(),
                                                right=Name(id='models_updated', ctx=Load()),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='idref', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='needs_update', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='env', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='api', ctx=Load()),
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
                                If(
                                    test=Name(id='perform_checks', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='module', ctx=Load()),
                                                    attr='_check',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='package', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='to upgrade', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='module', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='module', ctx=Load()),
                                                            attr='get_values_from_terp',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='package', ctx=Load()),
                                                                attr='data',
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
                                Expr(
                                    value=Call(
                                        func=Name(id='load_data', ctx=Load()),
                                        args=[
                                            Name(id='cr', ctx=Load()),
                                            Name(id='idref', ctx=Load()),
                                            Name(id='mode', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='kind',
                                                value=Constant(value='data', kind=None),
                                            ),
                                            keyword(
                                                arg='package',
                                                value=Name(id='package', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Name(id='demo_loaded', ctx=Store()),
                                        Attribute(
                                            value=Name(id='package', ctx=Load()),
                                            attr='dbdemo',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='load_demo', ctx=Load()),
                                        args=[
                                            Name(id='cr', ctx=Load()),
                                            Name(id='package', ctx=Load()),
                                            Name(id='idref', ctx=Load()),
                                            Name(id='mode', ctx=Load()),
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
                                            Constant(value='update ir_module_module set demo=%s where id=%s', kind=None),
                                            Tuple(
                                                elts=[
                                                    Name(id='demo_loaded', ctx=Load()),
                                                    Name(id='module_id', ctx=Load()),
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
                                            value=Name(id='module', ctx=Load()),
                                            attr='invalidate_cache',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[Constant(value='demo', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='migrations', ctx=Load()),
                                            attr='migrate_module',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='package', ctx=Load()),
                                            Constant(value='post', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='overwrite', ctx=Store())],
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
                                        slice=Constant(value='overwrite_existing_translations', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='module', ctx=Load()),
                                            attr='_update_translations',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='overwrite',
                                                value=Name(id='overwrite', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='package', ctx=Load()),
                                    attr='name',
                                    ctx=Load(),
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='registry', ctx=Load()),
                                                attr='_init_modules',
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='package', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='needs_update', ctx=Load()),
                            body=[
                                If(
                                    test=Name(id='new_install', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='post_init', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='package', ctx=Load()),
                                                        attr='info',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='post_init_hook', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='post_init', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Call(
                                                            func=Name(id='getattr', ctx=Load()),
                                                            args=[
                                                                Name(id='py_module', ctx=Load()),
                                                                Name(id='post_init', ctx=Load()),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        args=[
                                                            Name(id='cr', ctx=Load()),
                                                            Name(id='registry', ctx=Load()),
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
                                    test=Compare(
                                        left=Name(id='mode', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='update', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='env', ctx=Load()),
                                                        slice=Constant(value='ir.ui.view', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_validate_module_views',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='module_name', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
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
                                Assign(
                                    targets=[Name(id='concrete_models', ctx=Store())],
                                    value=ListComp(
                                        elt=Name(id='model', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='model', ctx=Store()),
                                                iter=Name(id='model_names', ctx=Load()),
                                                ifs=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='registry', ctx=Load()),
                                                                slice=Name(id='model', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            attr='_abstract',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='concrete_models', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='cr', ctx=Load()),
                                                    attr='execute',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='\n                    SELECT model FROM ir_model \n                    WHERE id NOT IN (SELECT DISTINCT model_id FROM ir_model_access) AND model IN %s\n                ', kind=None),
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Name(id='tuple', ctx=Load()),
                                                                args=[Name(id='concrete_models', ctx=Load())],
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
                                            targets=[Name(id='models', ctx=Store())],
                                            value=ListComp(
                                                elt=Name(id='model', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=List(
                                                            elts=[Name(id='model', ctx=Store())],
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
                                        If(
                                            test=Name(id='models', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='lines', ctx=Store())],
                                                    value=List(
                                                        elts=[
                                                            JoinedStr(
                                                                values=[
                                                                    Constant(value='The models ', kind=None),
                                                                    FormattedValue(
                                                                        value=Name(id='models', ctx=Load()),
                                                                        conversion=-1,
                                                                        format_spec=None,
                                                                    ),
                                                                    Constant(value=' have no access rules in module ', kind=None),
                                                                    FormattedValue(
                                                                        value=Name(id='module_name', ctx=Load()),
                                                                        conversion=-1,
                                                                        format_spec=None,
                                                                    ),
                                                                    Constant(value=', consider adding some, like:', kind=None),
                                                                ],
                                                            ),
                                                            Constant(value='id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                For(
                                                    target=Name(id='model', ctx=Store()),
                                                    iter=Name(id='models', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='xmlid', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='model', ctx=Load()),
                                                                    attr='replace',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='.', kind=None),
                                                                    Constant(value='_', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='lines', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    JoinedStr(
                                                                        values=[
                                                                            FormattedValue(
                                                                                value=Name(id='module_name', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value='.access_', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='xmlid', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value=',access_', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='xmlid', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value=',', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='module_name', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value='.model_', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='xmlid', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value=',base.group_user,1,0,0,0', kind=None),
                                                                        ],
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
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Constant(value='\n', kind=None),
                                                                    attr='join',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='lines', ctx=Load())],
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
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='updating', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='tools', ctx=Load()),
                                                attr='config',
                                                ctx=Load(),
                                            ),
                                            attr='options',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='init', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='tools', ctx=Load()),
                                                attr='config',
                                                ctx=Load(),
                                            ),
                                            attr='options',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='update', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Name(id='test_time', ctx=Store()),
                                Name(id='test_queries', ctx=Store()),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='test_results', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='tools', ctx=Load()),
                                                attr='config',
                                                ctx=Load(),
                                            ),
                                            attr='options',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='test_enable', kind=None),
                                        ctx=Load(),
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='needs_update', ctx=Load()),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='updating', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='env', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='api', ctx=Load()),
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
                                Assign(
                                    targets=[Name(id='loader', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='tests',
                                            ctx=Load(),
                                        ),
                                        attr='loader',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='suite', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='loader', ctx=Load()),
                                            attr='make_suite',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[Name(id='module_name', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                            Constant(value='at_install', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='suite', ctx=Load()),
                                            attr='countTestCases',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='needs_update', ctx=Load()),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='registry', ctx=Load()),
                                                            attr='setup_models',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='cr', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='env', ctx=Load()),
                                                        slice=Constant(value='ir.http', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_clear_routing_map',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='tests_t0', ctx=Store()),
                                                        Name(id='tests_q0', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='time', ctx=Load()),
                                                            attr='time',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='odoo', ctx=Load()),
                                                            attr='sql_db',
                                                            ctx=Load(),
                                                        ),
                                                        attr='sql_counter',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='test_results', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='loader', ctx=Load()),
                                                    attr='run_suite',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='suite', ctx=Load()),
                                                    Name(id='module_name', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='report', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='test_results', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='test_time', ctx=Store())],
                                            value=BinOp(
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
                                                right=Name(id='tests_t0', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='test_queries', ctx=Store())],
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='odoo', ctx=Load()),
                                                        attr='sql_db',
                                                        ctx=Load(),
                                                    ),
                                                    attr='sql_counter',
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=Name(id='tests_q0', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='env', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='api', ctx=Load()),
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
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='needs_update', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='processed_modules', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='package', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='ver', ctx=Store())],
                                    value=Call(
                                        func=Name(id='adapt_version', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='package', ctx=Load()),
                                                    attr='data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='version', kind=None),
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
                                            value=Name(id='module', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='state', kind=None),
                                                    Constant(value='latest_version', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='installed', kind=None),
                                                    Name(id='ver', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='package', ctx=Load()),
                                            attr='load_state',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='package', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='package', ctx=Load()),
                                            attr='load_version',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='package', ctx=Load()),
                                        attr='installed_version',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='package', ctx=Load()),
                                            attr='state',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='installed', kind=None),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='kind', ctx=Store()),
                                    iter=Tuple(
                                        elts=[
                                            Constant(value='init', kind=None),
                                            Constant(value='demo', kind=None),
                                            Constant(value='update', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Name(id='hasattr', ctx=Load()),
                                                args=[
                                                    Name(id='package', ctx=Load()),
                                                    Name(id='kind', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='delattr', ctx=Load()),
                                                        args=[
                                                            Name(id='package', ctx=Load()),
                                                            Name(id='kind', ctx=Load()),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='module', ctx=Load()),
                                            attr='flush',
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
                            targets=[Name(id='extra_queries', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='sql_db',
                                            ctx=Load(),
                                        ),
                                        attr='sql_counter',
                                        ctx=Load(),
                                    ),
                                    op=Sub(),
                                    right=Name(id='module_extra_query_count', ctx=Load()),
                                ),
                                op=Sub(),
                                right=Name(id='test_queries', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='extras', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='test_queries', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='extras', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            JoinedStr(
                                                values=[
                                                    Constant(value='+', kind=None),
                                                    FormattedValue(
                                                        value=Name(id='test_queries', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=' test', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='extra_queries', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='extras', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            JoinedStr(
                                                values=[
                                                    Constant(value='+', kind=None),
                                                    FormattedValue(
                                                        value=Name(id='extra_queries', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=' other', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='log',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='module_log_level', ctx=Load()),
                                    Constant(value='Module %s loaded in %.2fs%s, %s queries%s', kind=None),
                                    Name(id='module_name', ctx=Load()),
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
                                        right=Name(id='module_t0', ctx=Load()),
                                    ),
                                    IfExp(
                                        test=Name(id='test_time', ctx=Load()),
                                        body=JoinedStr(
                                            values=[
                                                Constant(value=' (incl. ', kind=None),
                                                FormattedValue(
                                                    value=Name(id='test_time', ctx=Load()),
                                                    conversion=-1,
                                                    format_spec=JoinedStr(
                                                        values=[Constant(value='.2f', kind=None)],
                                                    ),
                                                ),
                                                Constant(value='s test)', kind=None),
                                            ],
                                        ),
                                        orelse=Constant(value='', kind=None),
                                    ),
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='sql_log_count',
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=Name(id='module_cursor_query_count', ctx=Load()),
                                    ),
                                    IfExp(
                                        test=Name(id='extras', ctx=Load()),
                                        body=JoinedStr(
                                            values=[
                                                Constant(value=' (', kind=None),
                                                FormattedValue(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Constant(value=', ', kind=None),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='extras', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    conversion=-1,
                                                    format_spec=None,
                                                ),
                                                Constant(value=')', kind=None),
                                            ],
                                        ),
                                        orelse=Constant(value='', kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='test_results', ctx=Load()),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='test_results', ctx=Load()),
                                                attr='wasSuccessful',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='error',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Module %s: %d failures, %d errors of %d tests', kind=None),
                                            Name(id='module_name', ctx=Load()),
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='test_results', ctx=Load()),
                                                        attr='failures',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='test_results', ctx=Load()),
                                                        attr='errors',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='test_results', ctx=Load()),
                                                attr='testsRun',
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
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='_logger', ctx=Load()),
                            attr='runbot',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='%s modules loaded in %.2fs, %s queries (+%s extra)', kind=None),
                            Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='graph', ctx=Load())],
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
                                right=Name(id='t0', ctx=Load()),
                            ),
                            BinOp(
                                left=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='sql_log_count',
                                    ctx=Load(),
                                ),
                                op=Sub(),
                                right=Name(id='loading_cursor_query_count', ctx=Load()),
                            ),
                            BinOp(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='sql_db',
                                        ctx=Load(),
                                    ),
                                    attr='sql_counter',
                                    ctx=Load(),
                                ),
                                op=Sub(),
                                right=Name(id='loading_extra_query_count', ctx=Load()),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Tuple(
                        elts=[
                            Name(id='loaded_modules', ctx=Load()),
                            Name(id='processed_modules', ctx=Load()),
                        ],
                        ctx=Load(),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_check_module_names',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='module_names', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='mod_names', ctx=Store())],
                    value=Call(
                        func=Name(id='set', ctx=Load()),
                        args=[Name(id='module_names', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Constant(value='base', kind=None),
                        ops=[In()],
                        comparators=[Name(id='mod_names', ctx=Load())],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Constant(value='all', kind=None),
                                ops=[In()],
                                comparators=[Name(id='mod_names', ctx=Load())],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mod_names', ctx=Load()),
                                            attr='remove',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='all', kind=None)],
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
                    test=Name(id='mod_names', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='SELECT count(id) AS count FROM ir_module_module WHERE name in %s', kind=None),
                                    Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[Name(id='mod_names', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='dictfetchone',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    slice=Constant(value='count', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='mod_names', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='SELECT name FROM ir_module_module', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='incorrect_names', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mod_names', ctx=Load()),
                                            attr='difference',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            ListComp(
                                                elt=Subscript(
                                                    value=Name(id='x', ctx=Load()),
                                                    slice=Constant(value='name', kind=None),
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='x', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='cr', ctx=Load()),
                                                                attr='dictfetchall',
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
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='invalid module names, ignored: %s', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value=', ', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='incorrect_names', ctx=Load())],
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
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='load_marked_modules',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='graph', annotation=None, type_comment=None),
                    arg(arg='states', annotation=None, type_comment=None),
                    arg(arg='force', annotation=None, type_comment=None),
                    arg(arg='progressdict', annotation=None, type_comment=None),
                    arg(arg='report', annotation=None, type_comment=None),
                    arg(arg='loaded_modules', annotation=None, type_comment=None),
                    arg(arg='perform_checks', annotation=None, type_comment=None),
                    arg(arg='models_to_check', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value='Loads modules marked with ``states``, adding them to ``graph`` and\n       ``loaded_modules`` and returns a list of installed/upgraded modules.', kind=None),
                ),
                If(
                    test=Compare(
                        left=Name(id='models_to_check', ctx=Load()),
                        ops=[Is()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='models_to_check', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='processed_modules', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                While(
                    test=Constant(value=True, kind=None),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='SELECT name from ir_module_module WHERE state IN %s', kind=None),
                                    Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[Name(id='states', ctx=Load())],
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
                            targets=[Name(id='module_list', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='name', ctx=Load()),
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
                                        ifs=[
                                            Compare(
                                                left=Name(id='name', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[Name(id='graph', ctx=Load())],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='module_list', ctx=Load()),
                            ),
                            body=[Break()],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='graph', ctx=Load()),
                                    attr='add_modules',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='cr', ctx=Load()),
                                    Name(id='module_list', ctx=Load()),
                                    Name(id='force', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='debug',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Updating graph with %d more modules', kind=None),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='module_list', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='loaded', ctx=Store()),
                                        Name(id='processed', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='load_module_graph', ctx=Load()),
                                args=[
                                    Name(id='cr', ctx=Load()),
                                    Name(id='graph', ctx=Load()),
                                    Name(id='progressdict', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='report',
                                        value=Name(id='report', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='skip_modules',
                                        value=Name(id='loaded_modules', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='perform_checks',
                                        value=Name(id='perform_checks', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='models_to_check',
                                        value=Name(id='models_to_check', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='processed_modules', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[Name(id='processed', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='loaded_modules', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[Name(id='loaded', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='processed', ctx=Load()),
                            ),
                            body=[Break()],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='processed_modules', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='load_modules',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='registry', annotation=None, type_comment=None),
                    arg(arg='force_demo', annotation=None, type_comment=None),
                    arg(arg='status', annotation=None, type_comment=None),
                    arg(arg='update_module', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=False, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=False, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=' Load the modules for a registry object that has just been created.  This\n        function is part of Registry.new() and should not be used anywhere else.\n    ', kind=None),
                ),
                Expr(
                    value=Call(
                        func=Name(id='initialize_sys_path', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='force', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                If(
                    test=Name(id='force_demo', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='force', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='demo', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='models_to_check', ctx=Store())],
                    value=Call(
                        func=Name(id='set', ctx=Load()),
                        args=[],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[Constant(value="SET SESSION lock_timeout = '15s'", kind=None)],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
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
                                        attr='is_initialized',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='cr', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='update_module', ctx=Load()),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Database %s not initialized, you can force it with `-i base`', kind=None),
                                                    Attribute(
                                                        value=Name(id='cr', ctx=Load()),
                                                        attr='dbname',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Return(value=None),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='init db', kind=None)],
                                        keywords=[],
                                    ),
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
                                    targets=[Name(id='update_module', ctx=Store())],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='config',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='init', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='all', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=1, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Subscript(
                                            value=Attribute(
                                                value=Name(id='tools', ctx=Load()),
                                                attr='config',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='without_demo', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='tools', ctx=Load()),
                                                            attr='config',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='demo', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='all', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=1, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Constant(value='base', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='config',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='update', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Constant(value='all', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='config',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='update', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
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
                                            Constant(value='update ir_module_module set state=%s where name=%s and state=%s', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='to upgrade', kind=None),
                                                    Constant(value='base', kind=None),
                                                    Constant(value='installed', kind=None),
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
                        Assign(
                            targets=[Name(id='graph', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='modules',
                                            ctx=Load(),
                                        ),
                                        attr='graph',
                                        ctx=Load(),
                                    ),
                                    attr='Graph',
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
                                    value=Name(id='graph', ctx=Load()),
                                    attr='add_module',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='cr', ctx=Load()),
                                    Constant(value='base', kind=None),
                                    Name(id='force', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='graph', ctx=Load()),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='critical',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='module base cannot be loaded! (hint: verify addons-path)', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id='ImportError', ctx=Load()),
                                        args=[Constant(value='Module `base` cannot be loaded! (hint: verify addons-path)', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='report', ctx=Store())],
                            value=Attribute(
                                value=Name(id='registry', ctx=Load()),
                                attr='_assertion_report',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='loaded_modules', ctx=Store()),
                                        Name(id='processed_modules', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='load_module_graph', ctx=Load()),
                                args=[
                                    Name(id='cr', ctx=Load()),
                                    Name(id='graph', ctx=Load()),
                                    Name(id='status', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='perform_checks',
                                        value=Name(id='update_module', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='report',
                                        value=Name(id='report', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='models_to_check',
                                        value=Name(id='models_to_check', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='load_lang', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='tools', ctx=Load()),
                                        attr='config',
                                        ctx=Load(),
                                    ),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='load_language', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='load_lang', ctx=Load()),
                                    Name(id='update_module', ctx=Load()),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='registry', ctx=Load()),
                                            attr='setup_models',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='cr', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='load_lang', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='lang', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='load_lang', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=',', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='load_language',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='cr', ctx=Load()),
                                                    Name(id='lang', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='update_module', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='env', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='api', ctx=Load()),
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
                                Assign(
                                    targets=[Name(id='Module', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='env', ctx=Load()),
                                        slice=Constant(value='ir.module.module', kind=None),
                                        ctx=Load(),
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
                                        args=[Constant(value='updating modules list', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Module', ctx=Load()),
                                            attr='update_list',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='_check_module_names', ctx=Load()),
                                        args=[
                                            Name(id='cr', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='itertools', ctx=Load()),
                                                    attr='chain',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='tools', ctx=Load()),
                                                            attr='config',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='init', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='tools', ctx=Load()),
                                                            attr='config',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='update', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='module_names', ctx=Store())],
                                    value=ListComp(
                                        elt=Name(id='k', ctx=Load()),
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
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='tools', ctx=Load()),
                                                                attr='config',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='init', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='items',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[Name(id='v', ctx=Load())],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='module_names', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='modules', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Module', ctx=Load()),
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
                                                                    Constant(value='uninstalled', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='in', kind=None),
                                                                    Name(id='module_names', ctx=Load()),
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
                                            test=Name(id='modules', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='modules', ctx=Load()),
                                                            attr='button_install',
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
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='module_names', ctx=Store())],
                                    value=ListComp(
                                        elt=Name(id='k', ctx=Load()),
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
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='tools', ctx=Load()),
                                                                attr='config',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='update', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='items',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[Name(id='v', ctx=Load())],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='module_names', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='modules', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Module', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='state', kind=None),
                                                                    Constant(value='in', kind=None),
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='installed', kind=None),
                                                                            Constant(value='to upgrade', kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='in', kind=None),
                                                                    Name(id='module_names', ctx=Load()),
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
                                            test=Name(id='modules', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='modules', ctx=Load()),
                                                            attr='button_upgrade',
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
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='update ir_module_module set state=%s where name=%s', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='installed', kind=None),
                                                    Constant(value='base', kind=None),
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
                                            value=Name(id='Module', ctx=Load()),
                                            attr='invalidate_cache',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[Constant(value='state', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Module', ctx=Load()),
                                            attr='flush',
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
                            targets=[Name(id='previously_processed', ctx=Store())],
                            value=UnaryOp(
                                op=USub(),
                                operand=Constant(value=1, kind=None),
                            ),
                            type_comment=None,
                        ),
                        While(
                            test=Compare(
                                left=Name(id='previously_processed', ctx=Load()),
                                ops=[Lt()],
                                comparators=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='processed_modules', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='previously_processed', ctx=Store())],
                                    value=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='processed_modules', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='processed_modules', ctx=Store()),
                                    op=Add(),
                                    value=Call(
                                        func=Name(id='load_marked_modules', ctx=Load()),
                                        args=[
                                            Name(id='cr', ctx=Load()),
                                            Name(id='graph', ctx=Load()),
                                            List(
                                                elts=[
                                                    Constant(value='installed', kind=None),
                                                    Constant(value='to upgrade', kind=None),
                                                    Constant(value='to remove', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Name(id='force', ctx=Load()),
                                            Name(id='status', ctx=Load()),
                                            Name(id='report', ctx=Load()),
                                            Name(id='loaded_modules', ctx=Load()),
                                            Name(id='update_module', ctx=Load()),
                                            Name(id='models_to_check', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Name(id='update_module', ctx=Load()),
                                    body=[
                                        AugAssign(
                                            target=Name(id='processed_modules', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Name(id='load_marked_modules', ctx=Load()),
                                                args=[
                                                    Name(id='cr', ctx=Load()),
                                                    Name(id='graph', ctx=Load()),
                                                    List(
                                                        elts=[Constant(value='to install', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='force', ctx=Load()),
                                                    Name(id='status', ctx=Load()),
                                                    Name(id='report', ctx=Load()),
                                                    Name(id='loaded_modules', ctx=Load()),
                                                    Name(id='update_module', ctx=Load()),
                                                    Name(id='models_to_check', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[Constant(value="SELECT name from ir_module_module WHERE state = 'installed' and name != 'studio_customization'", kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='module_list', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='name', ctx=Load()),
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
                                        ifs=[
                                            Compare(
                                                left=Name(id='name', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[Name(id='graph', ctx=Load())],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='module_list', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='error',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Some modules are not loaded, some dependencies or manifest may be missing: %s', kind=None),
                                            Call(
                                                func=Name(id='sorted', ctx=Load()),
                                                args=[Name(id='module_list', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='registry', ctx=Load()),
                                    attr='loaded',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='registry', ctx=Load()),
                                    attr='setup_models',
                                    ctx=Load(),
                                ),
                                args=[Name(id='cr', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='migrations', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='modules',
                                            ctx=Load(),
                                        ),
                                        attr='migration',
                                        ctx=Load(),
                                    ),
                                    attr='MigrationManager',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='cr', ctx=Load()),
                                    Name(id='graph', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='package', ctx=Store()),
                            iter=Name(id='graph', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='migrations', ctx=Load()),
                                            attr='migrate_module',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='package', ctx=Load()),
                                            Constant(value='end', kind=None),
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
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[Constant(value="SELECT name from ir_module_module WHERE state IN ('to install', 'to upgrade')", kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='module_list', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='name', ctx=Load()),
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
                        If(
                            test=Name(id='module_list', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='error',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Some modules have inconsistent states, some dependencies may be missing: %s', kind=None),
                                            Call(
                                                func=Name(id='sorted', ctx=Load()),
                                                args=[Name(id='module_list', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='registry', ctx=Load()),
                                    attr='finalize_constraints',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='processed_modules', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='env', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='api', ctx=Load()),
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
                                            value=Name(id='cr', ctx=Load()),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='SELECT model from ir_model', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Tuple(
                                        elts=[Name(id='model', ctx=Store())],
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
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='model', ctx=Load()),
                                                ops=[In()],
                                                comparators=[Name(id='registry', ctx=Load())],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='env', ctx=Load()),
                                                                slice=Name(id='model', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            attr='_check_removed_columns',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='log',
                                                                value=Constant(value=True, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='isEnabledFor',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='logging', ctx=Load()),
                                                                attr='INFO',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='runbot',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='Model %s is declared but cannot be loaded! (Perhaps a module was partially removed or renamed)', kind=None),
                                                                    Name(id='model', ctx=Load()),
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
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='env', ctx=Load()),
                                                slice=Constant(value='ir.model.data', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_process_end',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='processed_modules', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='env', ctx=Load()),
                                                slice=Constant(value='base', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='kind', ctx=Store()),
                            iter=Tuple(
                                elts=[
                                    Constant(value='init', kind=None),
                                    Constant(value='demo', kind=None),
                                    Constant(value='update', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='tools', ctx=Load()),
                                                attr='config',
                                                ctx=Load(),
                                            ),
                                            slice=Name(id='kind', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='update_module', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='SELECT name, id FROM ir_module_module WHERE state=%s', kind=None),
                                            Tuple(
                                                elts=[Constant(value='to remove', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='modules_to_remove', ctx=Store())],
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
                                If(
                                    test=Name(id='modules_to_remove', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='env', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='api', ctx=Load()),
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
                                        Assign(
                                            targets=[Name(id='pkgs', ctx=Store())],
                                            value=Call(
                                                func=Name(id='reversed', ctx=Load()),
                                                args=[
                                                    ListComp(
                                                        elt=Name(id='p', ctx=Load()),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='p', ctx=Store()),
                                                                iter=Name(id='graph', ctx=Load()),
                                                                ifs=[
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='p', ctx=Load()),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[In()],
                                                                        comparators=[Name(id='modules_to_remove', ctx=Load())],
                                                                    ),
                                                                ],
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
                                            target=Name(id='pkg', ctx=Store()),
                                            iter=Name(id='pkgs', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='uninstall_hook', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='pkg', ctx=Load()),
                                                                attr='info',
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='uninstall_hook', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='uninstall_hook', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='py_module', ctx=Store())],
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='sys', ctx=Load()),
                                                                    attr='modules',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=BinOp(
                                                                    left=Constant(value='odoo.addons.%s', kind=None),
                                                                    op=Mod(),
                                                                    right=Tuple(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='pkg', ctx=Load()),
                                                                                attr='name',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Call(
                                                                    func=Name(id='getattr', ctx=Load()),
                                                                    args=[
                                                                        Name(id='py_module', ctx=Load()),
                                                                        Name(id='uninstall_hook', ctx=Load()),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                args=[
                                                                    Name(id='cr', ctx=Load()),
                                                                    Name(id='registry', ctx=Load()),
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
                                        Assign(
                                            targets=[Name(id='Module', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='env', ctx=Load()),
                                                slice=Constant(value='ir.module.module', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='Module', ctx=Load()),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='modules_to_remove', ctx=Load()),
                                                                    attr='values',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='module_uninstall',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='info',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='Reloading registry once more after uninstalling modules', kind=None)],
                                                keywords=[],
                                            ),
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
                                                    Attribute(
                                                        value=Name(id='cr', ctx=Load()),
                                                        attr='dbname',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='force_demo', ctx=Load()),
                                                    Name(id='status', ctx=Load()),
                                                    Name(id='update_module', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='cr', ctx=Load()),
                                                    attr='reset',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='registry', ctx=Load()),
                                                    attr='check_tables_exist',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='cr', ctx=Load())],
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
                                        Return(
                                            value=Name(id='registry', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='models_to_check', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='registry', ctx=Load()),
                                            attr='init_models',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='cr', ctx=Load()),
                                            Call(
                                                func=Name(id='list', ctx=Load()),
                                                args=[Name(id='models_to_check', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Dict(
                                                keys=[Constant(value='models_to_check', kind=None)],
                                                values=[Constant(value=True, kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='update_module', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='env', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='api', ctx=Load()),
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
                                                slice=Constant(value='res.groups', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_update_user_groups_view',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='View', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='env', ctx=Load()),
                                        slice=Constant(value='ir.ui.view', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='model', ctx=Store()),
                                    iter=Name(id='registry', ctx=Load()),
                                    body=[
                                        Try(
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='View', ctx=Load()),
                                                            attr='_validate_custom_views',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='model', ctx=Load())],
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
                                                                    attr='warning',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='invalid custom view(s) for model %s: %s', kind=None),
                                                                    Name(id='model', ctx=Load()),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='tools', ctx=Load()),
                                                                            attr='ustr',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='e', ctx=Load())],
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
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='report', ctx=Load()),
                                    attr='wasSuccessful',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                        args=[Constant(value='Modules loaded.', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='error',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='At least one test failed when loading the modules.', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='env', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='api', ctx=Load()),
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
                        For(
                            target=Name(id='model', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='env', ctx=Load()),
                                    attr='values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='model', ctx=Load()),
                                            attr='_register_hook',
                                            ctx=Load(),
                                        ),
                                        args=[],
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
                                    value=Subscript(
                                        value=Name(id='env', ctx=Load()),
                                        slice=Constant(value='base', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Name(id='registry', ctx=Load()),
                                attr='updated_modules',
                                ctx=Store(),
                            ),
                            op=Add(),
                            value=Name(id='processed_modules', ctx=Load()),
                        ),
                    ],
                    type_comment=None,
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='reset_modules_state',
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
                Expr(
                    value=Constant(value='\n    Resets modules flagged as "to x" to their original state\n    ', kind=None),
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
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[Constant(value="UPDATE ir_module_module SET state='installed' WHERE state IN ('to remove', 'to upgrade')", kind=None)],
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
                                args=[Constant(value="UPDATE ir_module_module SET state='uninstalled' WHERE state='to install'", kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='warning',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Transient module states were reset', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    type_comment=None,
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
