Module(
    body=[
        Expr(
            value=Constant(value=' Modules dependency graph. ', kind=None),
        ),
        Import(
            names=[alias(name='itertools', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        Import(
            names=[alias(name='odoo.tools', asname='tools')],
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
            name='Graph',
            bases=[Name(id='dict', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Modules dependency graph.\n\n    The graph is a mapping from module name to Nodes.\n\n    ', kind=None),
                ),
                FunctionDef(
                    name='add_node',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='info', annotation=None, type_comment=None),
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
                                Tuple(
                                    elts=[
                                        Name(id='max_depth', ctx=Store()),
                                        Name(id='father', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Constant(value=0, kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='d', ctx=Store()),
                            iter=Subscript(
                                value=Name(id='info', ctx=Load()),
                                slice=Constant(value='depends', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='n', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='d', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='Node', ctx=Load()),
                                                args=[
                                                    Name(id='d', ctx=Load()),
                                                    Name(id='self', ctx=Load()),
                                                    Constant(value=None, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='n', ctx=Load()),
                                            attr='depth',
                                            ctx=Load(),
                                        ),
                                        ops=[GtE()],
                                        comparators=[Name(id='max_depth', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='father', ctx=Store())],
                                            value=Name(id='n', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='max_depth', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='n', ctx=Load()),
                                                attr='depth',
                                                ctx=Load(),
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
                            test=Name(id='father', ctx=Load()),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='father', ctx=Load()),
                                            attr='add_child',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='name', ctx=Load()),
                                            Name(id='info', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Call(
                                        func=Name(id='Node', ctx=Load()),
                                        args=[
                                            Name(id='name', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                            Name(id='info', ctx=Load()),
                                        ],
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
                    name='update_from_db',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='cr', annotation=None, type_comment=None),
                        ],
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
                                operand=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='self', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='additional_data', ctx=Store())],
                            value=DictComp(
                                key=Name(id='key', ctx=Load()),
                                value=Dict(
                                    keys=[
                                        Constant(value='id', kind=None),
                                        Constant(value='state', kind=None),
                                        Constant(value='dbdemo', kind=None),
                                        Constant(value='installed_version', kind=None),
                                    ],
                                    values=[
                                        Constant(value=0, kind=None),
                                        Constant(value='uninstalled', kind=None),
                                        Constant(value=False, kind=None),
                                        Constant(value=None, kind=None),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='key', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='keys',
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
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='SELECT name, id, state, demo AS dbdemo, latest_version AS installed_version  FROM ir_module_module WHERE name IN %s', kind=None),
                                    Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[Name(id='additional_data', ctx=Load())],
                                                keywords=[],
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
                                    value=Name(id='additional_data', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    GeneratorExp(
                                        elt=Tuple(
                                            elts=[
                                                Subscript(
                                                    value=Name(id='x', ctx=Load()),
                                                    slice=Constant(value='name', kind=None),
                                                    ctx=Load(),
                                                ),
                                                Name(id='x', ctx=Load()),
                                            ],
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
                        ),
                        For(
                            target=Name(id='package', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                For(
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
                                                value=Name(id='additional_data', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='package', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='setattr', ctx=Load()),
                                                args=[
                                                    Name(id='package', ctx=Load()),
                                                    Name(id='k', ctx=Load()),
                                                    Name(id='v', ctx=Load()),
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='add_module',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='cr', annotation=None, type_comment=None),
                            arg(arg='module', annotation=None, type_comment=None),
                            arg(arg='force', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='add_modules',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='cr', ctx=Load()),
                                    List(
                                        elts=[Name(id='module', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                    Name(id='force', ctx=Load()),
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
                    name='add_modules',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='cr', annotation=None, type_comment=None),
                            arg(arg='module_list', annotation=None, type_comment=None),
                            arg(arg='force', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='force', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='force', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='packages', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='len_graph', ctx=Store())],
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='module', ctx=Store()),
                            iter=Name(id='module_list', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='info', ctx=Store())],
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
                                            attr='load_information_from_description_file',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='module', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='info', ctx=Load()),
                                            Subscript(
                                                value=Name(id='info', ctx=Load()),
                                                slice=Constant(value='installable', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='packages', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='module', ctx=Load()),
                                                            Name(id='info', ctx=Load()),
                                                        ],
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
                                                left=Name(id='module', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='studio_customization', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='module %s: not installable, skipped', kind=None),
                                                            Name(id='module', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='dependencies', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    ListComp(
                                        elt=Tuple(
                                            elts=[
                                                Name(id='p', ctx=Load()),
                                                Subscript(
                                                    value=Name(id='info', ctx=Load()),
                                                    slice=Constant(value='depends', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='p', ctx=Store()),
                                                        Name(id='info', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Name(id='packages', ctx=Load()),
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
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='current', ctx=Store()),
                                        Name(id='later', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Name(id='p', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Tuple(
                                                            elts=[
                                                                Name(id='p', ctx=Store()),
                                                                Name(id='info', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                        iter=Name(id='packages', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        While(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='packages', ctx=Load()),
                                    Compare(
                                        left=Name(id='current', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Name(id='later', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='package', ctx=Store()),
                                                Name(id='info', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='packages', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='deps', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='info', ctx=Load()),
                                        slice=Constant(value='depends', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='all', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Name(id='dep', ctx=Load()),
                                                    ops=[In()],
                                                    comparators=[Name(id='self', ctx=Load())],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='dep', ctx=Store()),
                                                        iter=Name(id='deps', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Compare(
                                                    left=Name(id='package', ctx=Load()),
                                                    ops=[In()],
                                                    comparators=[Name(id='current', ctx=Load())],
                                                ),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='packages', ctx=Load()),
                                                            attr='pop',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=0, kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Continue(),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='later', ctx=Load()),
                                                    attr='clear',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='current', ctx=Load()),
                                                    attr='remove',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='package', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='node', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='add_node',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='package', ctx=Load()),
                                                    Name(id='info', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
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
                                                    test=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='package', ctx=Load()),
                                                                ops=[In()],
                                                                comparators=[
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='tools', ctx=Load()),
                                                                            attr='config',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Name(id='kind', ctx=Load()),
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
                                                                        slice=Name(id='kind', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            Compare(
                                                                left=Name(id='kind', ctx=Load()),
                                                                ops=[In()],
                                                                comparators=[Name(id='force', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Name(id='setattr', ctx=Load()),
                                                                args=[
                                                                    Name(id='node', ctx=Load()),
                                                                    Name(id='kind', ctx=Load()),
                                                                    Constant(value=True, kind=None),
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
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='later', ctx=Load()),
                                                    attr='add',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='package', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='packages', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='package', ctx=Load()),
                                                            Name(id='info', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='packages', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0, kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='update_from_db',
                                    ctx=Load(),
                                ),
                                args=[Name(id='cr', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='package', ctx=Store()),
                            iter=Name(id='later', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='unmet_deps', ctx=Store())],
                                    value=ListComp(
                                        elt=Name(id='p', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='p', ctx=Store()),
                                                iter=Subscript(
                                                    value=Name(id='dependencies', ctx=Load()),
                                                    slice=Name(id='package', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                ifs=[
                                                    Compare(
                                                        left=Name(id='p', ctx=Load()),
                                                        ops=[NotIn()],
                                                        comparators=[Name(id='self', ctx=Load())],
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
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='module %s: Unmet dependencies: %s', kind=None),
                                            Name(id='package', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value=', ', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='unmet_deps', ctx=Load())],
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
                        Return(
                            value=BinOp(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='self', ctx=Load())],
                                    keywords=[],
                                ),
                                op=Sub(),
                                right=Name(id='len_graph', ctx=Load()),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__iter__',
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
                            targets=[Name(id='level', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='done', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='keys',
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
                        While(
                            test=Name(id='done', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='level_modules', ctx=Store())],
                                    value=Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Tuple(
                                                    elts=[
                                                        Name(id='name', ctx=Load()),
                                                        Name(id='module', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Tuple(
                                                            elts=[
                                                                Name(id='name', ctx=Store()),
                                                                Name(id='module', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='items',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ifs=[
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='module', ctx=Load()),
                                                                    attr='depth',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Name(id='level', ctx=Load())],
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
                                    target=Tuple(
                                        elts=[
                                            Name(id='name', ctx=Store()),
                                            Name(id='module', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Name(id='level_modules', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='done', ctx=Load()),
                                                    attr='remove',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='name', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Yield(
                                                value=Name(id='module', ctx=Load()),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='level', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
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
                    name='__str__',
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
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='\n', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Name(id='str', ctx=Load()),
                                            args=[Name(id='n', ctx=Load())],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='n', ctx=Store()),
                                                iter=Name(id='self', ctx=Load()),
                                                ifs=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='n', ctx=Load()),
                                                            attr='depth',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
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
        ClassDef(
            name='Node',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' One module in the modules dependency graph.\n\n    Node acts as a per-module singleton. A node is constructed via\n    Graph.add_module() or Graph.add_modules(). Some of its fields are from\n    ir_module_module (set by Graph.update_from_db()).\n\n    ', kind=None),
                ),
                FunctionDef(
                    name='__new__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='graph', annotation=None, type_comment=None),
                            arg(arg='info', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='name', ctx=Load()),
                                ops=[In()],
                                comparators=[Name(id='graph', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='inst', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='graph', ctx=Load()),
                                        slice=Name(id='name', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='inst', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='object', ctx=Load()),
                                            attr='__new__',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='cls', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='graph', ctx=Load()),
                                            slice=Name(id='name', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='inst', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='inst', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='graph', annotation=None, type_comment=None),
                            arg(arg='info', annotation=None, type_comment=None),
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
                                    attr='name',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='name', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='graph',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='graph', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='info',
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='info', ctx=Load()),
                                    Call(
                                        func=Name(id='getattr', ctx=Load()),
                                        args=[
                                            Name(id='self', ctx=Load()),
                                            Constant(value='info', kind=None),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='hasattr', ctx=Load()),
                                    args=[
                                        Name(id='self', ctx=Load()),
                                        Constant(value='children', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='children',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='hasattr', ctx=Load()),
                                    args=[
                                        Name(id='self', ctx=Load()),
                                        Constant(value='depth', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='depth',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
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
                    name='data',
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
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='info',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='add_child',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='info', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='node', ctx=Store())],
                            value=Call(
                                func=Name(id='Node', ctx=Load()),
                                args=[
                                    Name(id='name', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='graph',
                                        ctx=Load(),
                                    ),
                                    Name(id='info', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='node', ctx=Load()),
                                    attr='depth',
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='depth',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Constant(value=1, kind=None),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='node', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='children',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='children',
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='node', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='attr', ctx=Store()),
                            iter=Tuple(
                                elts=[
                                    Constant(value='init', kind=None),
                                    Constant(value='update', kind=None),
                                    Constant(value='demo', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='hasattr', ctx=Load()),
                                        args=[
                                            Name(id='self', ctx=Load()),
                                            Name(id='attr', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='setattr', ctx=Load()),
                                                args=[
                                                    Name(id='node', ctx=Load()),
                                                    Name(id='attr', ctx=Load()),
                                                    Constant(value=True, kind=None),
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='children',
                                        ctx=Load(),
                                    ),
                                    attr='sort',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='x', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Name(id='node', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__setattr__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
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
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Node', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__setattr__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='name', ctx=Load()),
                                    Name(id='value', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='name', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='init', kind=None),
                                            Constant(value='update', kind=None),
                                            Constant(value='demo', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
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
                                                slice=Name(id='name', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=1, kind=None),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='child', ctx=Store()),
                                    iter=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='children',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='setattr', ctx=Load()),
                                                args=[
                                                    Name(id='child', ctx=Load()),
                                                    Name(id='name', ctx=Load()),
                                                    Name(id='value', ctx=Load()),
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
                            test=Compare(
                                left=Name(id='name', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='depth', kind=None)],
                            ),
                            body=[
                                For(
                                    target=Name(id='child', ctx=Store()),
                                    iter=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='children',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='setattr', ctx=Load()),
                                                args=[
                                                    Name(id='child', ctx=Load()),
                                                    Name(id='name', ctx=Load()),
                                                    BinOp(
                                                        left=Name(id='value', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__iter__',
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='itertools', ctx=Load()),
                                    attr='chain',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='children',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='itertools', ctx=Load()),
                                                attr='chain',
                                                ctx=Load(),
                                            ),
                                            attr='from_iterable',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='children',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__str__',
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_pprint',
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
                    name='_pprint',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='depth', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=0, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='s', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='%s\n', kind=None),
                                op=Mod(),
                                right=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='name',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='c', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='children',
                                ctx=Load(),
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='s', ctx=Store()),
                                    op=Add(),
                                    value=BinOp(
                                        left=Constant(value='%s`-> %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                BinOp(
                                                    left=Constant(value='   ', kind=None),
                                                    op=Mult(),
                                                    right=Name(id='depth', ctx=Load()),
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='c', ctx=Load()),
                                                        attr='_pprint',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        BinOp(
                                                            left=Name(id='depth', ctx=Load()),
                                                            op=Add(),
                                                            right=Constant(value=1, kind=None),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='s', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='should_have_demo',
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
                            value=BoolOp(
                                op=And(),
                                values=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Name(id='hasattr', ctx=Load()),
                                                args=[
                                                    Name(id='self', ctx=Load()),
                                                    Constant(value='demo', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='dbdemo',
                                                        ctx=Load(),
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='state',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value='installed', kind=None)],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='all', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Attribute(
                                                    value=Name(id='p', ctx=Load()),
                                                    attr='dbdemo',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='p', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='parents',
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
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='parents',
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
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='depth',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=List(elts=[], ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=GeneratorExp(
                                elt=Name(id='node', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='node', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='graph',
                                                    ctx=Load(),
                                                ),
                                                attr='values',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='node', ctx=Load()),
                                                    attr='depth',
                                                    ctx=Load(),
                                                ),
                                                ops=[Lt()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='depth',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Name(id='self', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='node', ctx=Load()),
                                                        attr='children',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
