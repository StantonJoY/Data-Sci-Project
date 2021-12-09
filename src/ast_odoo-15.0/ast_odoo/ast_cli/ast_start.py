Module(
    body=[
        ImportFrom(
            module='__future__',
            names=[alias(name='print_function', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='argparse', asname=None)],
        ),
        Import(
            names=[alias(name='glob', asname=None)],
        ),
        Import(
            names=[alias(name='itertools', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='sys', asname=None)],
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            module=None,
            names=[alias(name='Command', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='server',
            names=[alias(name='main', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='odoo.modules.module',
            names=[
                alias(name='get_module_root', asname=None),
                alias(name='MANIFEST_NAMES', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.service.db',
            names=[
                alias(name='_create_empty_database', asname=None),
                alias(name='DatabaseExists', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='Start',
            bases=[Name(id='Command', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Quick start the Odoo server for your project', kind=None),
                ),
                FunctionDef(
                    name='get_module_list',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
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
                            targets=[Name(id='mods', ctx=Store())],
                            value=Call(
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
                                    GeneratorExp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Name(id='glob', ctx=Load()),
                                                attr='glob',
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
                                                        Name(id='path', ctx=Load()),
                                                        BinOp(
                                                            left=Constant(value='*/%s', kind=None),
                                                            op=Mod(),
                                                            right=Name(id='mname', ctx=Load()),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='mname', ctx=Store()),
                                                iter=Name(id='MANIFEST_NAMES', ctx=Load()),
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
                            value=ListComp(
                                elt=Subscript(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mod', ctx=Load()),
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
                                        operand=Constant(value=2, kind=None),
                                    ),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='mod', ctx=Store()),
                                        iter=Name(id='mods', ctx=Load()),
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
                    name='run',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='cmdargs', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
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
                                        arg='prog',
                                        value=BinOp(
                                            left=Constant(value='%s start', kind=None),
                                            op=Mod(),
                                            right=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='sys', ctx=Load()),
                                                                attr='argv',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
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
                                        ),
                                    ),
                                    keyword(
                                        arg='description',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='__doc__',
                                            ctx=Load(),
                                        ),
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
                                args=[Constant(value='--path', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='default',
                                        value=Constant(value='.', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value="Directory where your project's modules are stored (will autodetect from current dir)", kind=None),
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
                                    Constant(value='-d', kind=None),
                                    Constant(value='--database', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='db_name', kind=None),
                                    ),
                                    keyword(
                                        arg='default',
                                        value=Constant(value=None, kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value="Specify the database name (default to project's directory name", kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='args', ctx=Store()),
                                        Name(id='unknown', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='parse_known_args',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='args',
                                        value=Name(id='cmdargs', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='args', ctx=Load()),
                                            attr='path',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='.', kind=None)],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='environ',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='VIRTUAL_ENV', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='args', ctx=Load()),
                                            attr='path',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='environ',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='VIRTUAL_ENV', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='project_path', ctx=Store())],
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
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='expanduser',
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
                                                    attr='expandvars',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='args', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                            targets=[Name(id='module_root', ctx=Store())],
                            value=Call(
                                func=Name(id='get_module_root', ctx=Load()),
                                args=[Name(id='project_path', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='db_name', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='module_root', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='db_name', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='project_path', ctx=Load()),
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
                                    targets=[Name(id='project_path', ctx=Store())],
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
                                                    Name(id='project_path', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='pardir',
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
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='mods', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_module_list',
                                    ctx=Load(),
                                ),
                                args=[Name(id='project_path', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='mods', ctx=Load()),
                                    Compare(
                                        left=Constant(value='--addons-path', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='cmdargs', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cmdargs', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='--addons-path=%s', kind=None),
                                                op=Mod(),
                                                right=Name(id='project_path', ctx=Load()),
                                            ),
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
                                operand=Attribute(
                                    value=Name(id='args', ctx=Load()),
                                    attr='db_name',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='args', ctx=Load()),
                                            attr='db_name',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='db_name', ctx=Load()),
                                            Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='project_path', ctx=Load()),
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
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cmdargs', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='-d', kind=None),
                                                    Attribute(
                                                        value=Name(id='args', ctx=Load()),
                                                        attr='db_name',
                                                        ctx=Load(),
                                                    ),
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
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='_create_empty_database', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='db_name',
                                                ctx=Load(),
                                            ),
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
                                                slice=Constant(value='init', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='base', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='DatabaseExists', ctx=Load()),
                                    name='e',
                                    body=[Pass()],
                                ),
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='e',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='die', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='Could not create database `%s`. (%s)', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Attribute(
                                                                    value=Name(id='args', ctx=Load()),
                                                                    attr='db_name',
                                                                    ctx=Load(),
                                                                ),
                                                                Name(id='e', ctx=Load()),
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
                            orelse=[],
                            finalbody=[],
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='--db-filter', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='cmdargs', ctx=Load())],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cmdargs', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='--db-filter=^%s$', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='args', ctx=Load()),
                                                    attr='db_name',
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
                        FunctionDef(
                            name='to_remove',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='i', annotation=None, type_comment=None),
                                    arg(arg='l', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='l', ctx=Load()),
                                                    slice=Name(id='i', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='-p', kind=None)],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='l', ctx=Load()),
                                                        slice=Name(id='i', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='startswith',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='--path', kind=None)],
                                                keywords=[],
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='i', ctx=Load()),
                                                        ops=[Gt()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Subscript(
                                                            value=Name(id='l', ctx=Load()),
                                                            slice=BinOp(
                                                                left=Name(id='i', ctx=Load()),
                                                                op=Sub(),
                                                                right=Constant(value=1, kind=None),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='-p', kind=None),
                                                                    Constant(value='--path', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cmdargs', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='v', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='i', ctx=Store()),
                                                Name(id='v', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Name(id='enumerate', ctx=Load()),
                                            args=[Name(id='cmdargs', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ifs=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='to_remove', ctx=Load()),
                                                    args=[
                                                        Name(id='i', ctx=Load()),
                                                        Name(id='cmdargs', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
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
                                func=Name(id='main', ctx=Load()),
                                args=[Name(id='cmdargs', ctx=Load())],
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
            name='die',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='message', annotation=None, type_comment=None),
                    arg(arg='code', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=1, kind=None)],
            ),
            body=[
                Expr(
                    value=Call(
                        func=Name(id='print', ctx=Load()),
                        args=[Name(id='message', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='file',
                                value=Attribute(
                                    value=Name(id='sys', ctx=Load()),
                                    attr='stderr',
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='sys', ctx=Load()),
                            attr='exit',
                            ctx=Load(),
                        ),
                        args=[Name(id='code', ctx=Load())],
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
