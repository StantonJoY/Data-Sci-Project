Module(
    body=[
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='pkgutil', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='fields', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.tests.common',
            names=[alias(name='SavepointCaseWithUserDemo', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[alias(name='mute_logger', asname=None)],
            level=0,
        ),
        FunctionDef(
            name='message',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='msg', annotation=None, type_comment=None),
                    arg(arg='type', annotation=None, type_comment=None),
                    arg(arg='from_', annotation=None, type_comment=None),
                    arg(arg='to_', annotation=None, type_comment=None),
                    arg(arg='record', annotation=None, type_comment=None),
                    arg(arg='field', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                defaults=[
                    Constant(value='error', kind=None),
                    Constant(value=0, kind=None),
                    Constant(value=0, kind=None),
                    Constant(value=0, kind=None),
                    Constant(value='value', kind=None),
                ],
            ),
            body=[
                Return(
                    value=Call(
                        func=Name(id='dict', ctx=Load()),
                        args=[Name(id='kwargs', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='type',
                                value=Name(id='type', ctx=Load()),
                            ),
                            keyword(
                                arg='rows',
                                value=Dict(
                                    keys=[
                                        Constant(value='from', kind=None),
                                        Constant(value='to', kind=None),
                                    ],
                                    values=[
                                        Name(id='from_', ctx=Load()),
                                        Name(id='to_', ctx=Load()),
                                    ],
                                ),
                            ),
                            keyword(
                                arg='record',
                                value=Name(id='record', ctx=Load()),
                            ),
                            keyword(
                                arg='field',
                                value=Name(id='field', ctx=Load()),
                            ),
                            keyword(
                                arg='message',
                                value=Name(id='msg', ctx=Load()),
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
            name='moreaction',
            args=arguments(
                posonlyargs=[],
                args=[],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                defaults=[],
            ),
            body=[
                Return(
                    value=Call(
                        func=Name(id='dict', ctx=Load()),
                        args=[Name(id='kwargs', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='type',
                                value=Constant(value='ir.actions.act_window', kind=None),
                            ),
                            keyword(
                                arg='target',
                                value=Constant(value='new', kind=None),
                            ),
                            keyword(
                                arg='context',
                                value=Dict(
                                    keys=[Constant(value='create', kind=None)],
                                    values=[Constant(value=False, kind=None)],
                                ),
                            ),
                            keyword(
                                arg='name',
                                value=Constant(value='Possible Values', kind=None),
                            ),
                            keyword(
                                arg='view_mode',
                                value=Constant(value='tree,form', kind=None),
                            ),
                            keyword(
                                arg='views',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value=False, kind=None),
                                                Constant(value='list', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value=False, kind=None),
                                                Constant(value='form', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='See all possible values', kind='u'),
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
            name='values',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='seq', annotation=None, type_comment=None),
                    arg(arg='field', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value='value', kind=None)],
            ),
            body=[
                Return(
                    value=ListComp(
                        elt=Subscript(
                            value=Name(id='item', ctx=Load()),
                            slice=Name(id='field', ctx=Load()),
                            ctx=Load(),
                        ),
                        generators=[
                            comprehension(
                                target=Name(id='item', ctx=Store()),
                                iter=Name(id='seq', ctx=Load()),
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
        ClassDef(
            name='ImporterCase',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='TransactionCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='model_name', ctx=Store())],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ImporterCase', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='model',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='setUp',
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
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ImporterCase', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='model',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='model_name',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.data', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='clear_caches',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='cr',
                                            ctx=Load(),
                                        ),
                                        attr='cache',
                                        ctx=Load(),
                                    ),
                                    attr='clear',
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
                    name='import_',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                            arg(arg='rows', annotation=None, type_comment=None),
                            arg(arg='context', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='context', ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='context', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='import_file', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='model',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='context', ctx=Load()),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='load',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='fields', ctx=Load()),
                                    Name(id='rows', ctx=Load()),
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
                    name='read',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='context', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Tuple(
                                elts=[Constant(value='value', kind=None)],
                                ctx=Load(),
                            ),
                            Tuple(elts=[], ctx=Load()),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='records', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='model',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='context', ctx=Load()),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='records', ctx=Load()),
                                    attr='read',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fields', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='browse',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='context', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Tuple(elts=[], ctx=Load()),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='model',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='context', ctx=Load()),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='xid',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='ModelData', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.model.data', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ModelData', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='model', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='_name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
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
                            test=Name(id='data', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='d', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='data', ctx=Load()),
                                                attr='read',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                List(
                                                    elts=[
                                                        Constant(value='name', kind=None),
                                                        Constant(value='module', kind=None),
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
                                If(
                                    test=Subscript(
                                        value=Name(id='d', ctx=Load()),
                                        slice=Constant(value='module', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Return(
                                            value=BinOp(
                                                left=Constant(value='%s.%s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Subscript(
                                                            value=Name(id='d', ctx=Load()),
                                                            slice=Constant(value='module', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Subscript(
                                                            value=Name(id='d', ctx=Load()),
                                                            slice=Constant(value='name', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Subscript(
                                        value=Name(id='d', ctx=Load()),
                                        slice=Constant(value='name', kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='name', ctx=Store())],
                            value=Attribute(
                                value=Name(id='record', ctx=Load()),
                                attr='display_name',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='name', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='name', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='.', kind=None),
                                    Constant(value='-', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ModelData', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='model', kind=None),
                                            Constant(value='res_id', kind=None),
                                            Constant(value='module', kind=None),
                                        ],
                                        values=[
                                            Name(id='name', ctx=Load()),
                                            Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='_name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='__test__', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value='__test__.', kind=None),
                                op=Add(),
                                right=Name(id='name', ctx=Load()),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='add_translations',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='type', annotation=None, type_comment=None),
                            arg(arg='code', annotation=None, type_comment=None),
                        ],
                        vararg=arg(arg='tnx', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
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
                                    attr='_activate_lang',
                                    ctx=Load(),
                                ),
                                args=[Name(id='code', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='Translations', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.translation', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='source', ctx=Store()),
                                    Name(id='value', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='tnx', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Translations', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='lang', kind=None),
                                                    Constant(value='type', kind=None),
                                                    Constant(value='src', kind=None),
                                                    Constant(value='value', kind=None),
                                                    Constant(value='state', kind=None),
                                                ],
                                                values=[
                                                    Name(id='name', ctx=Load()),
                                                    Name(id='code', ctx=Load()),
                                                    Name(id='type', ctx=Load()),
                                                    Name(id='source', ctx=Load()),
                                                    Name(id='value', ctx=Load()),
                                                    Constant(value='translated', kind=None),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='test_ids_stuff',
            bases=[Name(id='ImporterCase', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='model_name', ctx=Store())],
                    value=Constant(value='export.integer', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_create_with_id',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='.id', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='42', kind=None),
                                                    Constant(value='36', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='type', kind=None),
                                                    Constant(value='rows', kind=None),
                                                    Constant(value='record', kind=None),
                                                    Constant(value='field', kind=None),
                                                    Constant(value='message', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='error', kind=None),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                    Constant(value=0, kind=None),
                                                    Constant(value='.id', kind=None),
                                                    Constant(value="Unknown database identifier '42'", kind='u'),
                                                ],
                                            ),
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
                    name='test_create_with_xid',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='somexmlid', kind=None),
                                                    Constant(value='42', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='__import__.somexmlid', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='xid',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='browse',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_update_with_id',
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
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='model',
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='value', kind=None)],
                                        values=[Constant(value=36, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=36, kind=None),
                                    Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='value',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='.id', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='record', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='42', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value=42, kind=None)],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_update_with_xid',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='somexmlid', kind=None),
                                                    Constant(value='36', kind=None),
                                                ],
                                                ctx=Load(),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value=36, kind=None)],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='somexmlid', kind=None),
                                                    Constant(value='1234567', kind=None),
                                                ],
                                                ctx=Load(),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value=1234567, kind=None)],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='test_boolean_field',
            bases=[Name(id='ImporterCase', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='model_name', ctx=Store())],
                    value=Constant(value='export.boolean', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_empty',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='import_',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[Constant(value='value', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='ids', kind=None),
                                            Constant(value='messages', kind=None),
                                            Constant(value='nextrow', kind=None),
                                        ],
                                        values=[
                                            List(elts=[], ctx=Load()),
                                            List(elts=[], ctx=Load()),
                                            Constant(value=False, kind=None),
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
                FunctionDef(
                    name='test_exported',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='False', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='True', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='records', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='read',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value=False, kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[Name(id='records', ctx=Load())],
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
                    name='test_falses',
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
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='lang', ctx=Store()),
                                    Name(id='source', ctx=Store()),
                                    Name(id='value', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='fr_FR', kind=None),
                                            Constant(value='no', kind=None),
                                            Constant(value='non', kind='u'),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='de_DE', kind=None),
                                            Constant(value='no', kind=None),
                                            Constant(value='nein', kind='u'),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='ru_RU', kind=None),
                                            Constant(value='no', kind=None),
                                            Constant(value='нет', kind='u'),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='nl_BE', kind=None),
                                            Constant(value='false', kind=None),
                                            Constant(value='vals', kind='u'),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='lt_LT', kind=None),
                                            Constant(value='false', kind=None),
                                            Constant(value='klaidingas', kind='u'),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='add_translations',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='test_import.py', kind=None),
                                            Constant(value='code', kind=None),
                                            Name(id='lang', ctx=Load()),
                                            Tuple(
                                                elts=[
                                                    Name(id='source', ctx=Load()),
                                                    Name(id='value', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='falses', ctx=Store())],
                            value=List(
                                elts=[
                                    List(
                                        elts=[Constant(value='0', kind='u')],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='no', kind='u')],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='false', kind='u')],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='FALSE', kind='u')],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='', kind='u')],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='non', kind='u')],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='nein', kind='u')],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='нет', kind='u')],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='vals', kind='u')],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='klaidingas', kind='u')],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    Name(id='falses', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='falses', ctx=Load())],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=List(
                                            elts=[Constant(value=False, kind=None)],
                                            ctx=Load(),
                                        ),
                                        op=Mult(),
                                        right=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='falses', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_trues',
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
                            targets=[Name(id='trues', ctx=Store())],
                            value=List(
                                elts=[
                                    List(
                                        elts=[Constant(value='None', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='nil', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='()', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='f', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='#f', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='VRAI', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='ok', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='true', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='yes', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='1', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    Name(id='trues', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='rows', kind=None),
                                                Constant(value='type', kind=None),
                                                Constant(value='record', kind=None),
                                                Constant(value='field', kind=None),
                                                Constant(value='message', kind=None),
                                                Constant(value='moreinfo', kind=None),
                                                Constant(value='field_name', kind=None),
                                            ],
                                            values=[
                                                Dict(
                                                    keys=[
                                                        Constant(value='from', kind=None),
                                                        Constant(value='to', kind=None),
                                                    ],
                                                    values=[
                                                        Name(id='i', ctx=Load()),
                                                        Name(id='i', ctx=Load()),
                                                    ],
                                                ),
                                                Constant(value='error', kind=None),
                                                Name(id='i', ctx=Load()),
                                                Constant(value='value', kind=None),
                                                BinOp(
                                                    left=Constant(value="Unknown value '%s' for boolean field 'Value'", kind=None),
                                                    op=Mod(),
                                                    right=Subscript(
                                                        value=Name(id='v', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Constant(value="Use '1' for yes and '0' for no", kind=None),
                                                Constant(value='Value', kind=None),
                                            ],
                                        ),
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
                                                    args=[Name(id='trues', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ifs=[
                                                    Compare(
                                                        left=Subscript(
                                                            value=Name(id='v', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotIn()],
                                                        comparators=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='true', kind=None),
                                                                    Constant(value='yes', kind=None),
                                                                    Constant(value='1', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
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
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='1', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='yes', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='true', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=List(
                                            elts=[Constant(value=True, kind=None)],
                                            ctx=Load(),
                                        ),
                                        op=Mult(),
                                        right=Constant(value=3, kind=None),
                                    ),
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='test_integer_field',
            bases=[Name(id='ImporterCase', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='model_name', ctx=Store())],
                    value=Constant(value='export.integer', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_none',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='import_',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[Constant(value='value', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='ids', kind=None),
                                            Constant(value='messages', kind=None),
                                            Constant(value='nextrow', kind=None),
                                        ],
                                        values=[
                                            List(elts=[], ctx=Load()),
                                            List(elts=[], ctx=Load()),
                                            Constant(value=False, kind=None),
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
                FunctionDef(
                    name='test_empty',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value=False, kind=None)],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_zero',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='0', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='-0', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_positives',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='1', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='42', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=BinOp(
                                                                    left=Constant(value=2, kind=None),
                                                                    op=Pow(),
                                                                    right=Constant(value=31, kind=None),
                                                                ),
                                                                op=Sub(),
                                                                right=Constant(value=1, kind=None),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='12345678', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=4, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value=1, kind=None),
                                            Constant(value=42, kind=None),
                                            BinOp(
                                                left=BinOp(
                                                    left=Constant(value=2, kind=None),
                                                    op=Pow(),
                                                    right=Constant(value=31, kind=None),
                                                ),
                                                op=Sub(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                            Constant(value=12345678, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_negatives',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='-1', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='-42', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=BinOp(
                                                                    left=BinOp(
                                                                        left=Constant(value=2, kind=None),
                                                                        op=Pow(),
                                                                        right=Constant(value=31, kind=None),
                                                                    ),
                                                                    op=Sub(),
                                                                    right=Constant(value=1, kind=None),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=BinOp(
                                                                    left=Constant(value=2, kind=None),
                                                                    op=Pow(),
                                                                    right=Constant(value=31, kind=None),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='-12345678', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=5, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=42, kind=None),
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=BinOp(
                                                    left=BinOp(
                                                        left=Constant(value=2, kind=None),
                                                        op=Pow(),
                                                        right=Constant(value=31, kind=None),
                                                    ),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=BinOp(
                                                    left=Constant(value=2, kind=None),
                                                    op=Pow(),
                                                    right=Constant(value=31, kind=None),
                                                ),
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=12345678, kind=None),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_out_of_range',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value=2, kind=None),
                                                                op=Pow(),
                                                                right=Constant(value=31, kind=None),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='type', kind=None),
                                                    Constant(value='rows', kind=None),
                                                    Constant(value='record', kind=None),
                                                    Constant(value='message', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='error', kind=None),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                    Constant(value=0, kind=None),
                                                    Constant(value='integer out of range\n', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=BinOp(
                                                                    left=Constant(value=2, kind=None),
                                                                    op=Pow(),
                                                                    right=Constant(value=32, kind=None),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='type', kind=None),
                                                    Constant(value='rows', kind=None),
                                                    Constant(value='record', kind=None),
                                                    Constant(value='message', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='error', kind=None),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                    Constant(value=0, kind=None),
                                                    Constant(value='integer out of range\n', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.sql_db', kind=None),
                                Constant(value='odoo.models', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_nonsense',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='zorglub', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='field_name', kind=None),
                                                    Constant(value='type', kind=None),
                                                    Constant(value='rows', kind=None),
                                                    Constant(value='record', kind=None),
                                                    Constant(value='field', kind=None),
                                                    Constant(value='message', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Value', kind=None),
                                                    Constant(value='error', kind=None),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                    Constant(value=0, kind=None),
                                                    Constant(value='value', kind=None),
                                                    Constant(value="'zorglub' does not seem to be an integer for field 'Value'", kind='u'),
                                                ],
                                            ),
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
        ClassDef(
            name='test_float_field',
            bases=[Name(id='ImporterCase', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='model_name', ctx=Store())],
                    value=Constant(value='export.float', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_none',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='import_',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[Constant(value='value', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='ids', kind=None),
                                            Constant(value='messages', kind=None),
                                            Constant(value='nextrow', kind=None),
                                        ],
                                        values=[
                                            List(elts=[], ctx=Load()),
                                            List(elts=[], ctx=Load()),
                                            Constant(value=False, kind=None),
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
                FunctionDef(
                    name='test_empty',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value=False, kind=None)],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_zero',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='0', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='-0', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_positives',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='1', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='42', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=BinOp(
                                                                    left=Constant(value=2, kind=None),
                                                                    op=Pow(),
                                                                    right=Constant(value=31, kind=None),
                                                                ),
                                                                op=Sub(),
                                                                right=Constant(value=1, kind=None),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='12345678', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value=2, kind=None),
                                                                op=Pow(),
                                                                right=Constant(value=33, kind=None),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='0.000001', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=6, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value=1, kind=None),
                                            Constant(value=42, kind=None),
                                            BinOp(
                                                left=BinOp(
                                                    left=Constant(value=2, kind=None),
                                                    op=Pow(),
                                                    right=Constant(value=31, kind=None),
                                                ),
                                                op=Sub(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                            Constant(value=12345678, kind=None),
                                            BinOp(
                                                left=Constant(value=2.0, kind=None),
                                                op=Pow(),
                                                right=Constant(value=33, kind=None),
                                            ),
                                            Constant(value=1e-06, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_negatives',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='-1', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='-42', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=UnaryOp(
                                                                    op=USub(),
                                                                    operand=BinOp(
                                                                        left=Constant(value=2, kind=None),
                                                                        op=Pow(),
                                                                        right=Constant(value=31, kind=None),
                                                                    ),
                                                                ),
                                                                op=Add(),
                                                                right=Constant(value=1, kind=None),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=BinOp(
                                                                    left=Constant(value=2, kind=None),
                                                                    op=Pow(),
                                                                    right=Constant(value=31, kind=None),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='-12345678', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=BinOp(
                                                                    left=Constant(value=2, kind=None),
                                                                    op=Pow(),
                                                                    right=Constant(value=33, kind=None),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='-0.000001', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=7, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=42, kind=None),
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=BinOp(
                                                    left=BinOp(
                                                        left=Constant(value=2, kind=None),
                                                        op=Pow(),
                                                        right=Constant(value=31, kind=None),
                                                    ),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=BinOp(
                                                    left=Constant(value=2, kind=None),
                                                    op=Pow(),
                                                    right=Constant(value=31, kind=None),
                                                ),
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=12345678, kind=None),
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=BinOp(
                                                    left=Constant(value=2.0, kind=None),
                                                    op=Pow(),
                                                    right=Constant(value=33, kind=None),
                                                ),
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1e-06, kind=None),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_nonsense',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='foobar', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='message', ctx=Load()),
                                                args=[Constant(value="'foobar' does not seem to be a number for field 'Value'", kind='u')],
                                                keywords=[
                                                    keyword(
                                                        arg='field_name',
                                                        value=Constant(value='Value', kind=None),
                                                    ),
                                                ],
                                            ),
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
        ClassDef(
            name='test_string_field',
            bases=[Name(id='ImporterCase', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='model_name', ctx=Store())],
                    value=Constant(value='export.string.bounded', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_empty',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value=False, kind=None)],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_imported',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='foobar', kind='u')],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='foobarbaz', kind='u')],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='Með suð í eyrum við spilum endalaust', kind='u')],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value="People 'get' types. They use them all the time. Telling someone he can't pound a nail with a banana doesn't much surprise him.", kind='u')],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=4, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='foobar', kind='u'),
                                            Constant(value='foobarbaz', kind='u'),
                                            Constant(value='Með suð í eyrum ', kind='u'),
                                            Constant(value="People 'get' typ", kind='u'),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='test_unbound_string_field',
            bases=[Name(id='ImporterCase', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='model_name', ctx=Store())],
                    value=Constant(value='export.string', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_imported',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='í dag viðrar vel til loftárása', kind='u')],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='If they ask you about fun, you tell them – fun is a filthy parasite', kind='u')],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='í dag viðrar vel til loftárása', kind='u'),
                                            Constant(value='If they ask you about fun, you tell them – fun is a filthy parasite', kind='u'),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='test_required_string_field',
            bases=[Name(id='ImporterCase', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='model_name', ctx=Store())],
                    value=Constant(value='export.string.required', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_empty',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[List(elts=[], ctx=Load())],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='message', ctx=Load()),
                                                args=[Constant(value="Missing required value for the field 'Value' (value)", kind='u')],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.sql_db', kind=None),
                                Constant(value='odoo.models', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_not_provided',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='const', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='12', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='message', ctx=Load()),
                                                args=[Constant(value="Missing required value for the field 'Value' (value)", kind='u')],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.sql_db', kind=None),
                                Constant(value='odoo.models', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_ignore_excess_messages',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='const', kind=None)],
                                        ctx=Load(),
                                    ),
                                    ListComp(
                                        elt=List(
                                            elts=[
                                                Call(
                                                    func=Name(id='str', ctx=Load()),
                                                    args=[Name(id='n', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='n', ctx=Store()),
                                                iter=Call(
                                                    func=Name(id='range', ctx=Load()),
                                                    args=[Constant(value=100, kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='messages', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=11, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='m', ctx=Store()),
                            iter=Subscript(
                                value=Subscript(
                                    value=Name(id='result', ctx=Load()),
                                    slice=Constant(value='messages', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Slice(
                                    lower=None,
                                    upper=UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='m', ctx=Load()),
                                                slice=Constant(value='type', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value='error', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='m', ctx=Load()),
                                                slice=Constant(value='message', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value="Missing required value for the field 'Value' (value)", kind='u'),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='last', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='result', ctx=Load()),
                                    slice=Constant(value='messages', kind=None),
                                    ctx=Load(),
                                ),
                                slice=UnaryOp(
                                    op=USub(),
                                    operand=Constant(value=1, kind=None),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='last', ctx=Load()),
                                        slice=Constant(value='type', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='warning', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='last', ctx=Load()),
                                        slice=Constant(value='message', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='Found more than 10 errors and more than one error per 10 records, interrupted to avoid showing too many errors.', kind='u'),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.sql_db', kind=None),
                                Constant(value='odoo.models', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='test_text',
            bases=[Name(id='ImporterCase', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='model_name', ctx=Store())],
                    value=Constant(value='export.text', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_empty',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value=False, kind=None)],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_imported',
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
                            targets=[Name(id='s', ctx=Store())],
                            value=Constant(value='Breiðskífa er notað um útgefna hljómplötu sem inniheldur stúdíóupptökur frá einum flytjanda. Breiðskífur eru oftast milli 25-80 mínútur og er lengd þeirra oft miðuð við 33⅓ snúninga 12 tommu vínylplötur (sem geta verið allt að 30 mín hvor hlið).\n\nBreiðskífur eru stundum tvöfaldar og eru þær þá gefnar út á tveimur geisladiskum eða tveimur vínylplötum.', kind='u'),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Name(id='s', ctx=Load())],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Name(id='s', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='test_selection',
            bases=[Name(id='ImporterCase', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='model_name', ctx=Store())],
                    value=Constant(value='export.selection', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='translations_fr', ctx=Store())],
                    value=List(
                        elts=[
                            Tuple(
                                elts=[
                                    Constant(value='Foo', kind=None),
                                    Constant(value='tete', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            Tuple(
                                elts=[
                                    Constant(value='Bar', kind=None),
                                    Constant(value='titi', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            Tuple(
                                elts=[
                                    Constant(value='Qux', kind=None),
                                    Constant(value='toto', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_imported',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='Qux', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='Bar', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='Foo', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='2', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=4, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='3', kind=None),
                                            Constant(value='2', kind=None),
                                            Constant(value='1', kind=None),
                                            Constant(value='2', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_imported_translated',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='add_translations',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ir.model.fields.selection,name', kind=None),
                                    Constant(value='model', kind=None),
                                    Constant(value='fr_FR', kind=None),
                                    Starred(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='translations_fr',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='toto', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='tete', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='titi', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='context',
                                        value=Dict(
                                            keys=[Constant(value='lang', kind=None)],
                                            values=[Constant(value='fr_FR', kind=None)],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='3', kind=None),
                                            Constant(value='1', kind=None),
                                            Constant(value='2', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='Foo', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='context',
                                        value=Dict(
                                            keys=[Constant(value='lang', kind=None)],
                                            values=[Constant(value='fr_FR', kind=None)],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                    name='test_invalid',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='Baz', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='message', ctx=Load()),
                                                args=[Constant(value="Value 'Baz' not found in selection field 'Value'", kind='u')],
                                                keywords=[
                                                    keyword(
                                                        arg='moreinfo',
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Constant(value='Foo Bar Qux 4', kind=None),
                                                                attr='split',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_name',
                                                        value=Constant(value='Value', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='field_path',
                                                        value=List(
                                                            elts=[Constant(value='value', kind=None)],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='42', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='message', ctx=Load()),
                                                args=[Constant(value="Value '42' not found in selection field 'Value'", kind='u')],
                                                keywords=[
                                                    keyword(
                                                        arg='moreinfo',
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Constant(value='Foo Bar Qux 4', kind=None),
                                                                attr='split',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_name',
                                                        value=Constant(value='Value', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='field_path',
                                                        value=List(
                                                            elts=[Constant(value='value', kind=None)],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
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
        ClassDef(
            name='test_selection_with_default',
            bases=[Name(id='ImporterCase', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='model_name', ctx=Store())],
                    value=Constant(value='export.selection.withdefault', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_empty',
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
                            value=Constant(value=' Empty cells should set corresponding field to False\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[Constant(value=False, kind=None)],
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
                    name='test_default',
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
                            value=Constant(value=' Non-provided cells should set corresponding field to default\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='const', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='42', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[Constant(value='2', kind=None)],
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
        ClassDef(
            name='test_selection_function',
            bases=[Name(id='ImporterCase', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='model_name', ctx=Store())],
                    value=Constant(value='export.selection.function', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='translations_fr', ctx=Store())],
                    value=List(
                        elts=[
                            Tuple(
                                elts=[
                                    Constant(value='Corge', kind=None),
                                    Constant(value='toto', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            Tuple(
                                elts=[
                                    Constant(value='Grault', kind=None),
                                    Constant(value='titi', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            Tuple(
                                elts=[
                                    Constant(value='Wheee', kind=None),
                                    Constant(value='tete', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            Tuple(
                                elts=[
                                    Constant(value='Moog', kind=None),
                                    Constant(value='tutu', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_imported',
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
                            value=Constant(value=' import uses fields_get, so translates import label (may or may not\n        be good news) *and* serializes the selection function to reverse it:\n        import does not actually know that the selection field uses a function\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='3', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='Grault', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='3', kind=None),
                                            Constant(value='1', kind=None),
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
                    name='test_translated',
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
                            value=Constant(value=' Expects output of selection function returns translated labels\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='add_translations',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ir.model.fields.selection,name', kind=None),
                                    Constant(value='model', kind=None),
                                    Constant(value='fr_FR', kind=None),
                                    Starred(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='translations_fr',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='titi', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='tete', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='context',
                                        value=Dict(
                                            keys=[Constant(value='lang', kind=None)],
                                            values=[Constant(value='fr_FR', kind=None)],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='1', kind=None),
                                            Constant(value='2', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='Wheee', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='context',
                                        value=Dict(
                                            keys=[Constant(value='lang', kind=None)],
                                            values=[Constant(value='fr_FR', kind=None)],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
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
            name='test_m2o',
            bases=[Name(id='ImporterCase', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='model_name', ctx=Store())],
                    value=Constant(value='export.many2one', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_by_name',
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
                            targets=[Name(id='record1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='export.integer', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='value', kind=None)],
                                        values=[Constant(value=42, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='record2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='export.integer', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='value', kind=None)],
                                        values=[Constant(value=36, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='name1', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Name(id='dict', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='record1', ctx=Load()),
                                                attr='name_get',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Name(id='record1', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='name2', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Name(id='dict', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='record2', ctx=Load()),
                                                attr='name_get',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Name(id='record2', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='_', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[Constant(value=5, kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='SAVEPOINT xxx', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='import_',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[Constant(value='value', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    List(
                                                        elts=[Name(id='name1', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[Name(id='name1', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[Name(id='name2', ctx=Load())],
                                                        ctx=Load(),
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
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='ROLLBACK TO SAVEPOINT xxx', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='RELEASE SAVEPOINT xxx', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=9, kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='import_',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[Constant(value='value', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    List(
                                                        elts=[Name(id='name1', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[Name(id='name1', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[Name(id='name2', ctx=Load())],
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
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='record1', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='name1', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='record1', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='name1', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='record2', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='name2', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_by_xid',
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
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='export.integer', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='value', kind=None)],
                                        values=[Constant(value=42, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='xid', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='xid',
                                    ctx=Load(),
                                ),
                                args=[Name(id='record', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value/id', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Name(id='xid', ctx=Load())],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='b', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=42, kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Subscript(
                                                value=Name(id='b', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='value',
                                            ctx=Load(),
                                        ),
                                        attr='value',
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
                    name='test_by_id',
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
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='export.integer', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='value', kind=None)],
                                        values=[Constant(value=42, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value/.id', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='b', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=42, kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Subscript(
                                                value=Name(id='b', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='value',
                                            ctx=Load(),
                                        ),
                                        attr='value',
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
                    name='test_by_names',
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
                            targets=[Name(id='record1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='export.integer', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='value', kind=None)],
                                        values=[Constant(value=42, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='record2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='export.integer', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='value', kind=None)],
                                        values=[Constant(value=42, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='name1', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Name(id='dict', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='record1', ctx=Load()),
                                                attr='name_get',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Name(id='record1', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='name2', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Name(id='dict', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='record2', ctx=Load()),
                                                attr='name_get',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Name(id='record2', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='name1', ctx=Load()),
                                    Name(id='name2', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Name(id='name2', ctx=Load())],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='message', ctx=Load()),
                                                args=[Constant(value="Found multiple matches for value 'export.integer:42' in field 'Value' (2 matches)", kind='u')],
                                                keywords=[
                                                    keyword(
                                                        arg='type',
                                                        value=Constant(value='warning', kind=None),
                                                    ),
                                                ],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='record1', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='name1', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_fail_by_implicit_id',
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
                            value=Constant(value=" Can't implicitly import records by id\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='record1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='export.integer', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='value', kind=None)],
                                        values=[Constant(value=42, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='record2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='export.integer', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='value', kind=None)],
                                        values=[Constant(value=36, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='record1', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='record2', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='record1', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    ListComp(
                                        elt=Call(
                                            func=Name(id='message', ctx=Load()),
                                            args=[
                                                BinOp(
                                                    left=Constant(value="No matching record found for name '%s' in field 'Value'", kind='u'),
                                                    op=Mod(),
                                                    right=Name(id='id', ctx=Load()),
                                                ),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='from_',
                                                    value=Name(id='index', ctx=Load()),
                                                ),
                                                keyword(
                                                    arg='to_',
                                                    value=Name(id='index', ctx=Load()),
                                                ),
                                                keyword(
                                                    arg='record',
                                                    value=Name(id='index', ctx=Load()),
                                                ),
                                                keyword(
                                                    arg='moreinfo',
                                                    value=Call(
                                                        func=Name(id='moreaction', ctx=Load()),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='res_model',
                                                                value=Constant(value='export.integer', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                keyword(
                                                    arg='field_name',
                                                    value=Constant(value='Value', kind=None),
                                                ),
                                                keyword(
                                                    arg='field_path',
                                                    value=List(
                                                        elts=[Constant(value='value', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                keyword(
                                                    arg='field_type',
                                                    value=Constant(value='name', kind=None),
                                                ),
                                                keyword(
                                                    arg='value',
                                                    value=Name(id='id', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='index', ctx=Store()),
                                                        Name(id='id', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Name(id='enumerate', ctx=Load()),
                                                    args=[
                                                        List(
                                                            elts=[
                                                                Attribute(
                                                                    value=Name(id='record1', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='record2', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='record1', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
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
                    name='test_fail_id_mistype',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value/.id', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='foo', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='message', ctx=Load()),
                                                args=[Constant(value="Invalid database id 'foo' for the field 'Value'", kind='u')],
                                                keywords=[
                                                    keyword(
                                                        arg='moreinfo',
                                                        value=Call(
                                                            func=Name(id='moreaction', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='res_model',
                                                                    value=Constant(value='ir.model.data', kind=None),
                                                                ),
                                                                keyword(
                                                                    arg='domain',
                                                                    value=List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='model', kind=None),
                                                                                    Constant(value='=', kind=None),
                                                                                    Constant(value='export.integer', kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_name',
                                                        value=Constant(value='Value', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='field_path',
                                                        value=List(
                                                            elts=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='.id', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
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
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.sql_db', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_sub_field',
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
                            value=Constant(value=" Does not implicitly create the record, does not warn that you can't\n        import m2o subfields (at all)...\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value/value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='42', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='message', ctx=Load()),
                                                args=[Constant(value='Can not create Many-To-One records indirectly, import the field separately', kind='u')],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
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
                    name='test_fail_noids',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='nameisnoexist:3', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='message', ctx=Load()),
                                                args=[Constant(value="No matching record found for name 'nameisnoexist:3' in field 'Value'", kind='u')],
                                                keywords=[
                                                    keyword(
                                                        arg='moreinfo',
                                                        value=Call(
                                                            func=Name(id='moreaction', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='res_model',
                                                                    value=Constant(value='export.integer', kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_name',
                                                        value=Constant(value='Value', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='field_path',
                                                        value=List(
                                                            elts=[Constant(value='value', kind=None)],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_type',
                                                        value=Constant(value='name', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='value',
                                                        value=Constant(value='nameisnoexist:3', kind=None),
                                                    ),
                                                ],
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
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value/id', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='noxidhere', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='message', ctx=Load()),
                                                args=[Constant(value="No matching record found for external id 'noxidhere' in field 'Value'", kind='u')],
                                                keywords=[
                                                    keyword(
                                                        arg='moreinfo',
                                                        value=Call(
                                                            func=Name(id='moreaction', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='res_model',
                                                                    value=Constant(value='ir.model.data', kind=None),
                                                                ),
                                                                keyword(
                                                                    arg='domain',
                                                                    value=List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='model', kind=None),
                                                                                    Constant(value='=', kind=None),
                                                                                    Constant(value='export.integer', kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_name',
                                                        value=Constant(value='Value', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='field_path',
                                                        value=List(
                                                            elts=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='id', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_type',
                                                        value=Constant(value='external id', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='value',
                                                        value=Constant(value='noxidhere', kind=None),
                                                    ),
                                                ],
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
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value/.id', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='66', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='message', ctx=Load()),
                                                args=[Constant(value="No matching record found for database id '66' in field 'Value'", kind='u')],
                                                keywords=[
                                                    keyword(
                                                        arg='moreinfo',
                                                        value=Call(
                                                            func=Name(id='moreaction', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='res_model',
                                                                    value=Constant(value='ir.model.data', kind=None),
                                                                ),
                                                                keyword(
                                                                    arg='domain',
                                                                    value=List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='model', kind=None),
                                                                                    Constant(value='=', kind=None),
                                                                                    Constant(value='export.integer', kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_name',
                                                        value=Constant(value='Value', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='field_path',
                                                        value=List(
                                                            elts=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='.id', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_type',
                                                        value=Constant(value='database id', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='value',
                                                        value=Constant(value='66', kind=None),
                                                    ),
                                                ],
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
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
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
                    name='test_fail_multiple',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='value', kind=None),
                                            Constant(value='value/id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='somename', kind=None),
                                                    Constant(value='somexid', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='message', ctx=Load()),
                                                args=[Constant(value="Ambiguous specification for field 'Value', only provide one of name, external id or database id", kind='u')],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
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
                    name='test_name_create_enabled_m2o',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value=101, kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='message', ctx=Load()),
                                                args=[Constant(value="No matching record found for name '101' in field 'Value'", kind='u')],
                                                keywords=[
                                                    keyword(
                                                        arg='moreinfo',
                                                        value=Call(
                                                            func=Name(id='moreaction', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='res_model',
                                                                    value=Constant(value='export.integer', kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_name',
                                                        value=Constant(value='Value', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='field_path',
                                                        value=List(
                                                            elts=[Constant(value='value', kind=None)],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_type',
                                                        value=Constant(value='name', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='value',
                                                        value=Constant(value=101, kind=None),
                                                    ),
                                                ],
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
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='name_create_enabled_fields', kind=None)],
                                values=[
                                    Dict(
                                        keys=[Constant(value='value', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value=101, kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='context',
                                        value=Name(id='context', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
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
            name='TestInvalidStrings',
            bases=[Name(id='ImporterCase', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='model_name', ctx=Store())],
                    value=Constant(value='export.m2o.str', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_fail_unpaired_surrogate',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='child_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='\uddff', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='surrogates', kind=None),
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='messages', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='message', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.sql_db', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_fail_nul',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='child_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='\x00', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='NUL', kind=None),
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='messages', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='message', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.sql_db', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='test_m2m',
            bases=[Name(id='ImporterCase', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='model_name', ctx=Store())],
                    value=Constant(value='export.many2many', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_ids',
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
                            targets=[Name(id='id1', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='export.many2many.other', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Dict(
                                            keys=[
                                                Constant(value='value', kind=None),
                                                Constant(value='str', kind=None),
                                            ],
                                            values=[
                                                Constant(value=3, kind=None),
                                                Constant(value='record0', kind=None),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='id2', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='export.many2many.other', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Dict(
                                            keys=[
                                                Constant(value='value', kind=None),
                                                Constant(value='str', kind=None),
                                            ],
                                            values=[
                                                Constant(value=44, kind=None),
                                                Constant(value='record1', kind=None),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='id3', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='export.many2many.other', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Dict(
                                            keys=[
                                                Constant(value='value', kind=None),
                                                Constant(value='str', kind=None),
                                            ],
                                            values=[
                                                Constant(value=84, kind=None),
                                                Constant(value='record2', kind=None),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='id4', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='export.many2many.other', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Dict(
                                            keys=[
                                                Constant(value='value', kind=None),
                                                Constant(value='str', kind=None),
                                            ],
                                            values=[
                                                Constant(value=9, kind=None),
                                                Constant(value='record3', kind=None),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='id5', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='export.many2many.other', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Dict(
                                            keys=[
                                                Constant(value='value', kind=None),
                                                Constant(value='str', kind=None),
                                            ],
                                            values=[
                                                Constant(value=99, kind=None),
                                                Constant(value='record4', kind=None),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value/.id', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    BinOp(
                                                        left=Constant(value='%d,%d', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='id1', ctx=Load()),
                                                                Name(id='id2', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    BinOp(
                                                        left=Constant(value='%d,%d,%d', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='id1', ctx=Load()),
                                                                Name(id='id3', ctx=Load()),
                                                                Name(id='id4', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    BinOp(
                                                        left=Constant(value='%d,%d,%d', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='id1', ctx=Load()),
                                                                Name(id='id2', ctx=Load()),
                                                                Name(id='id3', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    BinOp(
                                                        left=Constant(value='%d', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='id5', ctx=Load()),
                                                    ),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=4, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='ids', ctx=Store())],
                            value=Lambda(
                                args=arguments(
                                    posonlyargs=[],
                                    args=[arg(arg='records', annotation=None, type_comment=None)],
                                    vararg=None,
                                    kwonlyargs=[],
                                    kw_defaults=[],
                                    kwarg=None,
                                    defaults=[],
                                ),
                                body=ListComp(
                                    elt=Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    generators=[
                                        comprehension(
                                            target=Name(id='record', ctx=Store()),
                                            iter=Name(id='records', ctx=Load()),
                                            ifs=[],
                                            is_async=0,
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='b', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='ids', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='b', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='value',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Name(id='id1', ctx=Load()),
                                            Name(id='id2', ctx=Load()),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='b', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='value',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value=3, kind=None),
                                            Constant(value=44, kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='ids', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='b', ctx=Load()),
                                                    slice=Constant(value=2, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='value',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Name(id='id1', ctx=Load()),
                                            Name(id='id2', ctx=Load()),
                                            Name(id='id3', ctx=Load()),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='b', ctx=Load()),
                                                    slice=Constant(value=2, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='value',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value=3, kind=None),
                                            Constant(value=44, kind=None),
                                            Constant(value=84, kind=None),
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
                    name='test_noids',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value/.id', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='42', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='message', ctx=Load()),
                                                args=[Constant(value="No matching record found for database id '42' in field 'Value'", kind='u')],
                                                keywords=[
                                                    keyword(
                                                        arg='moreinfo',
                                                        value=Call(
                                                            func=Name(id='moreaction', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='res_model',
                                                                    value=Constant(value='ir.model.data', kind=None),
                                                                ),
                                                                keyword(
                                                                    arg='domain',
                                                                    value=List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='model', kind=None),
                                                                                    Constant(value='=', kind=None),
                                                                                    Constant(value='export.many2many.other', kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_name',
                                                        value=Constant(value='Value', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='field_path',
                                                        value=List(
                                                            elts=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='.id', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_type',
                                                        value=Constant(value='database id', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='value',
                                                        value=Constant(value='42', kind=None),
                                                    ),
                                                ],
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
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
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
                    name='test_xids',
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
                            targets=[Name(id='record0', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='export.many2many.other', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='value', kind=None),
                                            Constant(value='str', kind=None),
                                        ],
                                        values=[
                                            Constant(value=3, kind=None),
                                            Constant(value='record0', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='record1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='export.many2many.other', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='value', kind=None),
                                            Constant(value='str', kind=None),
                                        ],
                                        values=[
                                            Constant(value=44, kind=None),
                                            Constant(value='record1', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='record2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='export.many2many.other', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='value', kind=None),
                                            Constant(value='str', kind=None),
                                        ],
                                        values=[
                                            Constant(value=84, kind=None),
                                            Constant(value='record2', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='record3', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='export.many2many.other', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='value', kind=None),
                                            Constant(value='str', kind=None),
                                        ],
                                        values=[
                                            Constant(value=9, kind=None),
                                            Constant(value='record3', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value/id', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    BinOp(
                                                        left=Constant(value='%s,%s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='xid',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Name(id='record0', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='xid',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Name(id='record1', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    BinOp(
                                                        left=Constant(value='%s', kind=None),
                                                        op=Mod(),
                                                        right=Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='xid',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='record3', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    BinOp(
                                                        left=Constant(value='%s,%s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='xid',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Name(id='record2', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='xid',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Name(id='record1', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='b', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCountEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='b', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='value',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value=3, kind=None),
                                            Constant(value=44, kind=None),
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
                                    attr='assertCountEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='b', ctx=Load()),
                                                    slice=Constant(value=2, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='value',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value=44, kind=None),
                                            Constant(value=84, kind=None),
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
                    name='test_noxids',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value/id', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='noxidforthat', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='message', ctx=Load()),
                                                args=[Constant(value="No matching record found for external id 'noxidforthat' in field 'Value'", kind='u')],
                                                keywords=[
                                                    keyword(
                                                        arg='moreinfo',
                                                        value=Call(
                                                            func=Name(id='moreaction', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='res_model',
                                                                    value=Constant(value='ir.model.data', kind=None),
                                                                ),
                                                                keyword(
                                                                    arg='domain',
                                                                    value=List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='model', kind=None),
                                                                                    Constant(value='=', kind=None),
                                                                                    Constant(value='export.many2many.other', kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_name',
                                                        value=Constant(value='Value', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='field_path',
                                                        value=List(
                                                            elts=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='id', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_type',
                                                        value=Constant(value='external id', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='value',
                                                        value=Constant(value='noxidforthat', kind=None),
                                                    ),
                                                ],
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
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
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
                    name='test_names',
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
                            targets=[Name(id='record0', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='export.many2many.other', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='value', kind=None),
                                            Constant(value='str', kind=None),
                                        ],
                                        values=[
                                            Constant(value=3, kind=None),
                                            Constant(value='record0', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='record1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='export.many2many.other', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='value', kind=None),
                                            Constant(value='str', kind=None),
                                        ],
                                        values=[
                                            Constant(value=44, kind=None),
                                            Constant(value='record1', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='record2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='export.many2many.other', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='value', kind=None),
                                            Constant(value='str', kind=None),
                                        ],
                                        values=[
                                            Constant(value=84, kind=None),
                                            Constant(value='record2', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='record3', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='export.many2many.other', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='value', kind=None),
                                            Constant(value='str', kind=None),
                                        ],
                                        values=[
                                            Constant(value=9, kind=None),
                                            Constant(value='record3', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='name', ctx=Store())],
                            value=Lambda(
                                args=arguments(
                                    posonlyargs=[],
                                    args=[arg(arg='record', annotation=None, type_comment=None)],
                                    vararg=None,
                                    kwonlyargs=[],
                                    kw_defaults=[],
                                    kwarg=None,
                                    defaults=[],
                                ),
                                body=Attribute(
                                    value=Name(id='record', ctx=Load()),
                                    attr='display_name',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    BinOp(
                                                        left=Constant(value='%s,%s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Call(
                                                                    func=Name(id='name', ctx=Load()),
                                                                    args=[Name(id='record1', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                Call(
                                                                    func=Name(id='name', ctx=Load()),
                                                                    args=[Name(id='record2', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    BinOp(
                                                        left=Constant(value='%s,%s,%s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Call(
                                                                    func=Name(id='name', ctx=Load()),
                                                                    args=[Name(id='record0', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                Call(
                                                                    func=Name(id='name', ctx=Load()),
                                                                    args=[Name(id='record1', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                Call(
                                                                    func=Name(id='name', ctx=Load()),
                                                                    args=[Name(id='record2', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    BinOp(
                                                        left=Constant(value='%s,%s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Call(
                                                                    func=Name(id='name', ctx=Load()),
                                                                    args=[Name(id='record0', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                Call(
                                                                    func=Name(id='name', ctx=Load()),
                                                                    args=[Name(id='record3', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='b', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='b', ctx=Load()),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='value',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value=3, kind=None),
                                            Constant(value=44, kind=None),
                                            Constant(value=84, kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='b', ctx=Load()),
                                                    slice=Constant(value=2, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='value',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value=3, kind=None),
                                            Constant(value=9, kind=None),
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
                    name='test_nonames',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='wherethem2mhavenonames', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='message', ctx=Load()),
                                                args=[Constant(value="No matching record found for name 'wherethem2mhavenonames' in field 'Value'", kind='u')],
                                                keywords=[
                                                    keyword(
                                                        arg='moreinfo',
                                                        value=Call(
                                                            func=Name(id='moreaction', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='res_model',
                                                                    value=Constant(value='export.many2many.other', kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_name',
                                                        value=Constant(value='Value', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='field_path',
                                                        value=List(
                                                            elts=[Constant(value='value', kind=None)],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_type',
                                                        value=Constant(value='name', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='value',
                                                        value=Constant(value='wherethem2mhavenonames', kind=None),
                                                    ),
                                                ],
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
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
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
                    name='test_import_to_existing',
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
                            targets=[Name(id='id1', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='export.many2many.other', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Dict(
                                            keys=[
                                                Constant(value='value', kind=None),
                                                Constant(value='str', kind=None),
                                            ],
                                            values=[
                                                Constant(value=3, kind=None),
                                                Constant(value='record0', kind=None),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='id2', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='export.many2many.other', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Dict(
                                            keys=[
                                                Constant(value='value', kind=None),
                                                Constant(value='str', kind=None),
                                            ],
                                            values=[
                                                Constant(value=44, kind=None),
                                                Constant(value='record1', kind=None),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='id3', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='export.many2many.other', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Dict(
                                            keys=[
                                                Constant(value='value', kind=None),
                                                Constant(value='str', kind=None),
                                            ],
                                            values=[
                                                Constant(value=84, kind=None),
                                                Constant(value='record2', kind=None),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='id4', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='export.many2many.other', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Dict(
                                            keys=[
                                                Constant(value='value', kind=None),
                                                Constant(value='str', kind=None),
                                            ],
                                            values=[
                                                Constant(value=9, kind=None),
                                                Constant(value='record3', kind=None),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='xid', ctx=Store())],
                            value=Constant(value='myxid', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='value/.id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Name(id='xid', ctx=Load()),
                                                    BinOp(
                                                        left=Constant(value='%d,%d', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='id1', ctx=Load()),
                                                                Name(id='id2', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='value/.id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Name(id='xid', ctx=Load()),
                                                    BinOp(
                                                        left=Constant(value='%d,%d', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='id3', ctx=Load()),
                                                                Name(id='id4', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='b', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='b', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='b', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='value',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value=84, kind=None),
                                            Constant(value=9, kind=None),
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
        ClassDef(
            name='test_o2m',
            bases=[Name(id='ImporterCase', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='model_name', ctx=Store())],
                    value=Constant(value='export.one2many', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_name_get',
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
                            targets=[Name(id='s', ctx=Store())],
                            value=Constant(value='Java is a DSL for taking large XML files and converting them to stack traces', kind='u'),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='const', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='5', kind=None),
                                                    Name(id='s', ctx=Load()),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='message', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value="No matching record found for name '%s' in field 'Value'", kind='u'),
                                                        op=Mod(),
                                                        right=Subscript(
                                                            value=Name(id='s', ctx=Load()),
                                                            slice=Slice(
                                                                lower=None,
                                                                upper=Constant(value=50, kind=None),
                                                                step=None,
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='moreinfo',
                                                        value=Call(
                                                            func=Name(id='moreaction', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='res_model',
                                                                    value=Constant(value='export.one2many.child', kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_name',
                                                        value=Constant(value='Value', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='field_path',
                                                        value=List(
                                                            elts=[Constant(value='value', kind=None)],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_type',
                                                        value=Constant(value='name', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='value',
                                                        value=Subscript(
                                                            value=Name(id='s', ctx=Load()),
                                                            slice=Slice(
                                                                lower=None,
                                                                upper=Constant(value=50, kind=None),
                                                                step=None,
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
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
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
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
                    name='test_single',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='const', kind=None),
                                            Constant(value='value/value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='5', kind=None),
                                                    Constant(value='63', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[Name(id='b', ctx=Store())],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='b', ctx=Load()),
                                        attr='const',
                                        ctx=Load(),
                                    ),
                                    Constant(value=5, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='b', ctx=Load()),
                                                attr='value',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[Constant(value=63, kind=None)],
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
                    name='test_multicore',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='const', kind=None),
                                            Constant(value='value/value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='5', kind=None),
                                                    Constant(value='63', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='6', kind=None),
                                                    Constant(value='64', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='b1', ctx=Store()),
                                        Name(id='b2', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='b1', ctx=Load()),
                                        attr='const',
                                        ctx=Load(),
                                    ),
                                    Constant(value=5, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='b1', ctx=Load()),
                                                attr='value',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[Constant(value=63, kind=None)],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='b2', ctx=Load()),
                                        attr='const',
                                        ctx=Load(),
                                    ),
                                    Constant(value=6, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='b2', ctx=Load()),
                                                attr='value',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[Constant(value=64, kind=None)],
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
                    name='test_multisub',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='const', kind=None),
                                            Constant(value='value/value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='5', kind=None),
                                                    Constant(value='63', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='64', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='65', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='66', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[Name(id='b', ctx=Store())],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='values', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='b', ctx=Load()),
                                                        attr='value',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value=63, kind=None),
                                                    Constant(value=64, kind=None),
                                                    Constant(value=65, kind=None),
                                                    Constant(value=66, kind=None),
                                                ],
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
                    name='test_multi_subfields',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='value/str', kind=None),
                                            Constant(value='const', kind=None),
                                            Constant(value='value/value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='this', kind=None),
                                                    Constant(value='5', kind=None),
                                                    Constant(value='63', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='is', kind=None),
                                                    Constant(value='', kind=None),
                                                    Constant(value='64', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='the', kind=None),
                                                    Constant(value='', kind=None),
                                                    Constant(value='65', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='rhythm', kind=None),
                                                    Constant(value='', kind=None),
                                                    Constant(value='66', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[Name(id='b', ctx=Store())],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='values', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='b', ctx=Load()),
                                                                attr='value',
                                                                ctx=Load(),
                                                            ),
                                                            attr='sorted',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value=63, kind=None),
                                                    Constant(value=64, kind=None),
                                                    Constant(value=65, kind=None),
                                                    Constant(value=66, kind=None),
                                                ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='b', ctx=Load()),
                                                        attr='value',
                                                        ctx=Load(),
                                                    ),
                                                    attr='sorted',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Constant(value='str', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Constant(value='this is the rhythm', kind=None),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[],
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
                    name='test_subfields_fail_by_implicit_id',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value/parent_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='noxidforthat', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='message', ctx=Load()),
                                                args=[Constant(value="No matching record found for name 'noxidforthat' in field 'Value/Parent'", kind='u')],
                                                keywords=[
                                                    keyword(
                                                        arg='moreinfo',
                                                        value=Call(
                                                            func=Name(id='moreaction', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='res_model',
                                                                    value=Constant(value='export.one2many', kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_name',
                                                        value=Constant(value='Value', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='field_path',
                                                        value=List(
                                                            elts=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='parent_id', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_type',
                                                        value=Constant(value='name', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='value',
                                                        value=Constant(value='noxidforthat', kind=None),
                                                    ),
                                                ],
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
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
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
                    name='test_link_inline',
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
                            value=Constant(value=' m2m-style specification for o2ms\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='id1', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='export.one2many.child', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Dict(
                                            keys=[
                                                Constant(value='str', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            values=[
                                                Constant(value='Bf', kind=None),
                                                Constant(value=109, kind=None),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='id2', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='export.one2many.child', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Dict(
                                            keys=[
                                                Constant(value='str', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            values=[
                                                Constant(value='Me', kind=None),
                                                Constant(value=262, kind=None),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='const', kind=None),
                                            Constant(value='value/.id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='42', kind=None),
                                                    BinOp(
                                                        left=Constant(value='%d,%d', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='id1', ctx=Load()),
                                                                Name(id='id2', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                List(
                                    elts=[Name(id='b', ctx=Store())],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='b', ctx=Load()),
                                        attr='const',
                                        ctx=Load(),
                                    ),
                                    Constant(value=42, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='values', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='b', ctx=Load()),
                                                        attr='value',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value=109, kind=None),
                                                    Constant(value=262, kind=None),
                                                ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='b', ctx=Load()),
                                                attr='value',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='field',
                                                value=Constant(value='parent_id', kind=None),
                                            ),
                                        ],
                                    ),
                                    List(
                                        elts=[
                                            Name(id='b', ctx=Load()),
                                            Name(id='b', ctx=Load()),
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
                    name='test_link',
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
                            value=Constant(value=' O2M relating to an existing record (update) force a LINK_TO as well\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='id1', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='export.one2many.child', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Dict(
                                            keys=[
                                                Constant(value='str', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            values=[
                                                Constant(value='Bf', kind=None),
                                                Constant(value=109, kind=None),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='id2', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='export.one2many.child', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Dict(
                                            keys=[
                                                Constant(value='str', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            values=[
                                                Constant(value='Me', kind=None),
                                                Constant(value=262, kind=None),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='const', kind=None),
                                            Constant(value='value/.id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='42', kind=None),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='id1', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='id2', ctx=Load())],
                                                        keywords=[],
                                                    ),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                List(
                                    elts=[Name(id='b', ctx=Store())],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='b', ctx=Load()),
                                        attr='const',
                                        ctx=Load(),
                                    ),
                                    Constant(value=42, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCountEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='b', ctx=Load()),
                                                attr='value',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value=109, kind=None),
                                            Constant(value=262, kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='b', ctx=Load()),
                                                attr='value',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='field',
                                                value=Constant(value='parent_id', kind=None),
                                            ),
                                        ],
                                    ),
                                    List(
                                        elts=[
                                            Name(id='b', ctx=Load()),
                                            Name(id='b', ctx=Load()),
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
                    name='test_link_2',
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
                            targets=[Name(id='id1', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='export.one2many.child', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Dict(
                                            keys=[
                                                Constant(value='str', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            values=[
                                                Constant(value='Bf', kind=None),
                                                Constant(value=109, kind=None),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='id2', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='export.one2many.child', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Dict(
                                            keys=[
                                                Constant(value='str', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            values=[
                                                Constant(value='Me', kind=None),
                                                Constant(value=262, kind=None),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='const', kind=None),
                                            Constant(value='value/.id', kind=None),
                                            Constant(value='value/value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='42', kind=None),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='id1', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='1', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='id2', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='2', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                List(
                                    elts=[Name(id='b', ctx=Store())],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='b', ctx=Load()),
                                        attr='const',
                                        ctx=Load(),
                                    ),
                                    Constant(value=42, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='values', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='b', ctx=Load()),
                                                        attr='value',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=2, kind=None),
                                                ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='values', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='b', ctx=Load()),
                                                attr='value',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='field',
                                                value=Constant(value='parent_id', kind=None),
                                            ),
                                        ],
                                    ),
                                    List(
                                        elts=[
                                            Name(id='b', ctx=Load()),
                                            Name(id='b', ctx=Load()),
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
                    name='test_o2m_repeated_with_xids',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='const', kind=None),
                                            Constant(value='value/id', kind=None),
                                            Constant(value='value/value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='a', kind=None),
                                                    Constant(value='5', kind=None),
                                                    Constant(value='aa', kind=None),
                                                    Constant(value='11', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='', kind=None),
                                                    Constant(value='ab', kind=None),
                                                    Constant(value='12', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='', kind=None),
                                                    Constant(value='ac', kind=None),
                                                    Constant(value='13', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='', kind=None),
                                                    Constant(value='ad', kind=None),
                                                    Constant(value='14', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='b', kind=None),
                                                    Constant(value='10', kind=None),
                                                    Constant(value='ba', kind=None),
                                                    Constant(value='15', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='', kind=None),
                                                    Constant(value='bb', kind=None),
                                                    Constant(value='16', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='const', kind=None),
                                            Constant(value='value/id', kind=None),
                                            Constant(value='value/value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='a', kind=None),
                                                    Constant(value='5', kind=None),
                                                    Constant(value='aa', kind=None),
                                                    Constant(value='11', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='', kind=None),
                                                    Constant(value='ab', kind=None),
                                                    Constant(value='12', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='', kind=None),
                                                    Constant(value='ac', kind=None),
                                                    Constant(value='13', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='', kind=None),
                                                    Constant(value='ad', kind=None),
                                                    Constant(value='14', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='b', kind=None),
                                                    Constant(value='8', kind=None),
                                                    Constant(value='ba', kind=None),
                                                    Constant(value='25', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='', kind=None),
                                                    Constant(value='bb', kind=None),
                                                    Constant(value='16', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                List(
                                    elts=[
                                        Name(id='a', ctx=Store()),
                                        Name(id='b', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='sorted',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='r', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Attribute(
                                            value=Name(id='r', ctx=Load()),
                                            attr='const',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='a', ctx=Load()),
                                                attr='value',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=4, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='b', ctx=Load()),
                                                attr='value',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='b', ctx=Load()),
                                        attr='const',
                                        ctx=Load(),
                                    ),
                                    Constant(value=8, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='b', ctx=Load()),
                                                attr='value',
                                                ctx=Load(),
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='value', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value=25, kind=None),
                                            Constant(value=16, kind=None),
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
                    name='test_name_create_enabled_m2o_in_o2m',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value/m2o', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value=101, kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='message', ctx=Load()),
                                                args=[Constant(value="No matching record found for name '101' in field 'Value/M2O'", kind='u')],
                                                keywords=[
                                                    keyword(
                                                        arg='moreinfo',
                                                        value=Call(
                                                            func=Name(id='moreaction', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='res_model',
                                                                    value=Constant(value='export.integer', kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_name',
                                                        value=Constant(value='Value', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='field_path',
                                                        value=List(
                                                            elts=[
                                                                Constant(value='value', kind=None),
                                                                Constant(value='m2o', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_type',
                                                        value=Constant(value='name', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='value',
                                                        value=Constant(value=101, kind=None),
                                                    ),
                                                ],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='name_create_enabled_fields', kind=None)],
                                values=[
                                    Dict(
                                        keys=[Constant(value='value/m2o', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value/m2o', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value=101, kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='context',
                                        value=Name(id='context', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                List(
                                    elts=[Name(id='b', ctx=Store())],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='b', ctx=Load()),
                                                attr='value',
                                                ctx=Load(),
                                            ),
                                            attr='m2o',
                                            ctx=Load(),
                                        ),
                                        attr='value',
                                        ctx=Load(),
                                    ),
                                    Constant(value=101, kind=None),
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
            name='test_o2m_multiple',
            bases=[Name(id='ImporterCase', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='model_name', ctx=Store())],
                    value=Constant(value='export.one2many.multiple', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_multi_mixed',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='const', kind=None),
                                            Constant(value='child1/value', kind=None),
                                            Constant(value='child2/value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='5', kind=None),
                                                    Constant(value='11', kind=None),
                                                    Constant(value='21', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='12', kind=None),
                                                    Constant(value='22', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='13', kind=None),
                                                    Constant(value='23', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='14', kind=None),
                                                    Constant(value='', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                List(
                                    elts=[Name(id='b', ctx=Store())],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='values', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='b', ctx=Load()),
                                                        attr='child1',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value=11, kind=None),
                                                    Constant(value=12, kind=None),
                                                    Constant(value=13, kind=None),
                                                    Constant(value=14, kind=None),
                                                ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='values', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='b', ctx=Load()),
                                                        attr='child2',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value=21, kind=None),
                                                    Constant(value=22, kind=None),
                                                    Constant(value=23, kind=None),
                                                ],
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
                    name='test_multi',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='const', kind=None),
                                            Constant(value='child1/value', kind=None),
                                            Constant(value='child2/value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='5', kind=None),
                                                    Constant(value='11', kind=None),
                                                    Constant(value='21', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='12', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='13', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='14', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='', kind=None),
                                                    Constant(value='22', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='', kind=None),
                                                    Constant(value='23', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                List(
                                    elts=[Name(id='b', ctx=Store())],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='values', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='b', ctx=Load()),
                                                        attr='child1',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value=11, kind=None),
                                                    Constant(value=12, kind=None),
                                                    Constant(value=13, kind=None),
                                                    Constant(value=14, kind=None),
                                                ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='values', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='b', ctx=Load()),
                                                        attr='child2',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value=21, kind=None),
                                                    Constant(value=22, kind=None),
                                                    Constant(value=23, kind=None),
                                                ],
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
                    name='test_multi_fullsplit',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='const', kind=None),
                                            Constant(value='child1/value', kind=None),
                                            Constant(value='child2/value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='5', kind=None),
                                                    Constant(value='11', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='12', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='13', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='14', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='', kind=None),
                                                    Constant(value='21', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='', kind=None),
                                                    Constant(value='22', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='', kind=None),
                                                    Constant(value='23', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                List(
                                    elts=[Name(id='b', ctx=Store())],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='browse',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='b', ctx=Load()),
                                        attr='const',
                                        ctx=Load(),
                                    ),
                                    Constant(value=5, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='values', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='b', ctx=Load()),
                                                        attr='child1',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value=11, kind=None),
                                                    Constant(value=12, kind=None),
                                                    Constant(value=13, kind=None),
                                                    Constant(value=14, kind=None),
                                                ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='values', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='b', ctx=Load()),
                                                        attr='child2',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value=21, kind=None),
                                                    Constant(value=22, kind=None),
                                                    Constant(value=23, kind=None),
                                                ],
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='test_realworld',
            bases=[Name(id='SavepointCaseWithUserDemo', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
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
                                            Name(id='test_realworld', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_load_partners_set',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_bigfile',
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
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='json', ctx=Load()),
                                    attr='loads',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='pkgutil', ctx=Load()),
                                                    attr='get_data',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='__module__',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='contacts_big.json', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='decode',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='utf-8', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='load',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='mobile', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='image_1920', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='data', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='data', ctx=Load())],
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
                    name='test_backlink',
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
                            targets=[Name(id='fnames', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='name', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='street', kind=None),
                                    Constant(value='city', kind=None),
                                    Constant(value='country_id', kind=None),
                                    Constant(value='category_id', kind=None),
                                    Constant(value='is_company', kind=None),
                                    Constant(value='parent_id', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='json', ctx=Load()),
                                    attr='loads',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='pkgutil', ctx=Load()),
                                                    attr='get_data',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='__module__',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='contacts.json', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='decode',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='utf-8', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='load',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='fnames', ctx=Load()),
                                    Name(id='data', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='data', ctx=Load())],
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
                    name='test_recursive_o2m',
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
                            value=Constant(value=" The content of the o2m field's dict needs to go through conversion\n        as it may be composed of convertables or other relational fields\n        ", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.data', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='clear_caches',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='Model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='export.one2many.recursive', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Model', ctx=Load()),
                                    attr='load',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='value', kind=None),
                                            Constant(value='child/const', kind=None),
                                            Constant(value='child/child1/str', kind=None),
                                            Constant(value='child/child2/value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='4', kind=None),
                                                    Constant(value='42', kind=None),
                                                    Constant(value='foo', kind=None),
                                                    Constant(value='55', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='43', kind=None),
                                                    Constant(value='bar', kind=None),
                                                    Constant(value='56', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='', kind=None),
                                                    Constant(value='baz', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='55', kind=None),
                                                    Constant(value='qux', kind=None),
                                                    Constant(value='57', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='5', kind=None),
                                                    Constant(value='99', kind=None),
                                                    Constant(value='wheee', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='98', kind=None),
                                                    Constant(value='', kind=None),
                                                    Constant(value='12', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='b', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Model', ctx=Load()),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='b', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='value',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='b', ctx=Load()),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='value',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value=4, kind=None),
                                            Constant(value=5, kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Attribute(
                                            value=Name(id='child', ctx=Load()),
                                            attr='str',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='child', ctx=Store()),
                                                iter=Attribute(
                                                    value=Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Subscript(
                                                                        value=Name(id='b', ctx=Load()),
                                                                        slice=Constant(value=0, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='child',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='sorted',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='child1',
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='bar', kind=None),
                                            Constant(value='baz', kind=None),
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
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='b', ctx=Load()),
                                                                    slice=Constant(value=1, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='child',
                                                                ctx=Load(),
                                                            ),
                                                            attr='sorted',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='child1',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Attribute(
                                            value=Name(id='child', ctx=Load()),
                                            attr='value',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='child', ctx=Store()),
                                                iter=Attribute(
                                                    value=Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Subscript(
                                                                        value=Name(id='b', ctx=Load()),
                                                                        slice=Constant(value=1, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='child',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='sorted',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='child2',
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    List(
                                        elts=[Constant(value=12, kind=None)],
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
                    name='test_o2m_subfields_fail_by_implicit_id',
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.data', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='clear_caches',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='Model', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='export.one2many.recursive', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Model', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='import_file',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='load',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='child/child1/parent_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='5', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='message', ctx=Load()),
                                                args=[Constant(value="No matching record found for name '5' in field 'Child/Child1/Parent'", kind='u')],
                                                keywords=[
                                                    keyword(
                                                        arg='field',
                                                        value=Constant(value='child', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='moreinfo',
                                                        value=Call(
                                                            func=Name(id='moreaction', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='res_model',
                                                                    value=Constant(value='export.one2many.multiple', kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_name',
                                                        value=Constant(value='Child', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='field_path',
                                                        value=List(
                                                            elts=[
                                                                Constant(value='child', kind=None),
                                                                Constant(value='child1', kind=None),
                                                                Constant(value='parent_id', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_type',
                                                        value=Constant(value='name', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='value',
                                                        value=Constant(value='5', kind=None),
                                                    ),
                                                ],
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
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
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
            name='test_date',
            bases=[Name(id='ImporterCase', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='model_name', ctx=Store())],
                    value=Constant(value='export.date', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_empty',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='import_',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[Constant(value='value', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='ids', kind=None),
                                            Constant(value='messages', kind=None),
                                            Constant(value='nextrow', kind=None),
                                        ],
                                        values=[
                                            List(elts=[], ctx=Load()),
                                            List(elts=[], ctx=Load()),
                                            Constant(value=False, kind=None),
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
                FunctionDef(
                    name='test_basic',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='2012-02-03', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
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
                    name='test_invalid',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='not really a date', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='message', ctx=Load()),
                                                args=[Constant(value="'not really a date' does not seem to be a valid date for field 'Value'", kind='u')],
                                                keywords=[
                                                    keyword(
                                                        arg='moreinfo',
                                                        value=Constant(value="Use the format '2012-12-31'", kind='u'),
                                                    ),
                                                    keyword(
                                                        arg='field_name',
                                                        value=Constant(value='Value', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='field_path',
                                                        value=List(
                                                            elts=[Constant(value='value', kind=None)],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
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
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
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
            name='test_datetime',
            bases=[Name(id='ImporterCase', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='model_name', ctx=Store())],
                    value=Constant(value='export.datetime', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_empty',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='import_',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[Constant(value='value', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='ids', kind=None),
                                            Constant(value='messages', kind=None),
                                            Constant(value='nextrow', kind=None),
                                        ],
                                        values=[
                                            List(elts=[], ctx=Load()),
                                            List(elts=[], ctx=Load()),
                                            Constant(value=False, kind=None),
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
                FunctionDef(
                    name='test_basic',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='2012-02-03 11:11:11', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
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
                    name='test_invalid',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='not really a datetime', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='message', ctx=Load()),
                                                args=[Constant(value="'not really a datetime' does not seem to be a valid datetime for field 'Value'", kind='u')],
                                                keywords=[
                                                    keyword(
                                                        arg='moreinfo',
                                                        value=Constant(value="Use the format '2012-12-31 23:59:59'", kind='u'),
                                                    ),
                                                    keyword(
                                                        arg='field_name',
                                                        value=Constant(value='Value', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='field_path',
                                                        value=List(
                                                            elts=[Constant(value='value', kind=None)],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
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
                                    attr='assertIs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
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
                    name='test_checktz1',
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
                            value=Constant(value=' Imported date should be interpreted as being in the tz provided by\n        the context\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
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
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='tz', kind=None)],
                                        values=[Constant(value='Asia/Hovd', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='2012-02-03 11:11:11', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='tz', kind=None)],
                                        values=[Constant(value='Pacific/Kiritimati', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='fields', ctx=Load()),
                                                    attr='Datetime',
                                                    ctx=Load(),
                                                ),
                                                attr='to_string',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Subscript(
                                                    value=Name(id='value', ctx=Load()),
                                                    slice=Constant(value='value', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='value', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='read',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='domain',
                                                            value=List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='in', kind=None),
                                                                            Subscript(
                                                                                value=Name(id='result', ctx=Load()),
                                                                                slice=Constant(value='ids', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    List(
                                        elts=[Constant(value='2012-02-02 21:11:11', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='2012-02-03 11:11:11', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='tz', kind=None)],
                                        values=[Constant(value='Pacific/Marquesas', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='fields', ctx=Load()),
                                                    attr='Datetime',
                                                    ctx=Load(),
                                                ),
                                                attr='to_string',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Subscript(
                                                    value=Name(id='value', ctx=Load()),
                                                    slice=Constant(value='value', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='value', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='read',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='domain',
                                                            value=List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='in', kind=None),
                                                                            Subscript(
                                                                                value=Name(id='result', ctx=Load()),
                                                                                slice=Constant(value='ids', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    List(
                                        elts=[Constant(value='2012-02-03 20:41:11', kind=None)],
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
                    name='test_usertz',
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
                            value=Constant(value=" If the context does not hold a timezone, the importing user's tz\n        should be used\n        ", kind=None),
                        ),
                        Expr(
                            value=Call(
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
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='tz', kind=None)],
                                        values=[Constant(value='Asia/Yakutsk', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='2012-02-03 11:11:11', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='fields', ctx=Load()),
                                                    attr='Datetime',
                                                    ctx=Load(),
                                                ),
                                                attr='to_string',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Subscript(
                                                    value=Name(id='value', ctx=Load()),
                                                    slice=Constant(value='value', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='value', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='read',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='domain',
                                                            value=List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='in', kind=None),
                                                                            Subscript(
                                                                                value=Name(id='result', ctx=Load()),
                                                                                slice=Constant(value='ids', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    List(
                                        elts=[Constant(value='2012-02-03 01:11:11', kind=None)],
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
                    name='test_notz',
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
                            value=Constant(value=' If there is no tz either in the context or on the user, falls back\n        to UTC\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
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
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='tz', kind=None)],
                                        values=[Constant(value=False, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='2012-02-03 11:11:11', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='fields', ctx=Load()),
                                                    attr='Datetime',
                                                    ctx=Load(),
                                                ),
                                                attr='to_string',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Subscript(
                                                    value=Name(id='value', ctx=Load()),
                                                    slice=Constant(value='value', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='value', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='read',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='domain',
                                                            value=List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='in', kind=None),
                                                                            Subscript(
                                                                                value=Name(id='result', ctx=Load()),
                                                                                slice=Constant(value='ids', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    List(
                                        elts=[Constant(value='2012-02-03 11:11:11', kind=None)],
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
        ClassDef(
            name='test_unique',
            bases=[Name(id='ImporterCase', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='model_name', ctx=Store())],
                    value=Constant(value='export.unique', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_unique',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='1', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='1', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='2', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='3', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='3', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='message',
                                                        value=Constant(value="The value for the field 'value' already exists (this is probably 'Value' in the current model).", kind='u'),
                                                    ),
                                                    keyword(
                                                        arg='type',
                                                        value=Constant(value='error', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='rows',
                                                        value=Dict(
                                                            keys=[
                                                                Constant(value='from', kind=None),
                                                                Constant(value='to', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=1, kind=None),
                                                                Constant(value=1, kind=None),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='record',
                                                        value=Constant(value=1, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='field',
                                                        value=Constant(value='value', kind=None),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='message',
                                                        value=Constant(value="The value for the field 'value' already exists (this is probably 'Value' in the current model).", kind='u'),
                                                    ),
                                                    keyword(
                                                        arg='type',
                                                        value=Constant(value='error', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='rows',
                                                        value=Dict(
                                                            keys=[
                                                                Constant(value='from', kind=None),
                                                                Constant(value='to', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value=4, kind=None),
                                                                Constant(value=4, kind=None),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='record',
                                                        value=Constant(value=4, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='field',
                                                        value=Constant(value='value', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.sql_db', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_unique_pair',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='value2', kind=None),
                                            Constant(value='value3', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='0', kind=None),
                                                    Constant(value='1', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='1', kind=None),
                                                    Constant(value='0', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='1', kind=None),
                                                    Constant(value='1', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='1', kind=None),
                                                    Constant(value='1', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='messages', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='message', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='result', ctx=Load()),
                                    slice=Constant(value='messages', kind=None),
                                    ctx=Load(),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='message', ctx=Load()),
                                        slice=Constant(value='type', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='error', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='message', ctx=Load()),
                                        slice=Constant(value='record', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=3, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='message', ctx=Load()),
                                        slice=Constant(value='rows', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='from', kind=None),
                                            Constant(value='to', kind=None),
                                        ],
                                        values=[
                                            Constant(value=3, kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='m', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='match',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="The values for the fields '([^']+)' already exist \\(they are probably '([^']+)' in the current model\\)\\.", kind=None),
                                    Subscript(
                                        value=Name(id='message', ctx=Load()),
                                        slice=Constant(value='message', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIsNotNone',
                                    ctx=Load(),
                                ),
                                args=[Name(id='m', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='m', ctx=Load()),
                                                    attr='group',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=1, kind=None)],
                                                keywords=[],
                                            ),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=', ', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='value2', kind=None),
                                            Constant(value='value3', kind=None),
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
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='m', ctx=Load()),
                                                    attr='group',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=2, kind=None)],
                                                keywords=[],
                                            ),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=', ', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='Value2', kind=None),
                                            Constant(value='Value3', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.sql_db', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='test_inherits',
            bases=[Name(id='ImporterCase', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=" The import process should only assign a new xid (derived from the\n    childs') if the child is being created and triggers the creation of the\n    parent\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='model_name', ctx=Store())],
                    value=Constant(value='export.inherits.child', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_create_no_parent',
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
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='value_parent', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='xxx.child', kind=None),
                                                    Constant(value='0', kind=None),
                                                    Constant(value='1', kind=None),
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
                        Assign(
                            targets=[Name(id='rec', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='model_name',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='r', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='rec', ctx=Load()),
                                        attr='value_parent',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='rec', ctx=Load()),
                                        attr='value',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='parent_id',
                                            ctx=Load(),
                                        ),
                                        attr='value_parent',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='rec', ctx=Load()),
                                                attr='_get_external_ids',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        slice=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='xxx.child', kind=None)],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='parent_id',
                                                    ctx=Load(),
                                                ),
                                                attr='_get_external_ids',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        slice=Attribute(
                                            value=Attribute(
                                                value=Name(id='rec', ctx=Load()),
                                                attr='parent_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='xxx.child_export_inherits_parent', kind=None)],
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
                    name='test_create_parent_no_xid',
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
                            targets=[Name(id='parent', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='export.inherits.parent', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='value_parent', kind=None)],
                                        values=[Constant(value=0, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='parent_id/.id', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='xxx.child', kind=None),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='parent', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='1', kind=None),
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
                        Assign(
                            targets=[Name(id='rec', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='model_name',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='r', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='rec', ctx=Load()),
                                        attr='value_parent',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='rec', ctx=Load()),
                                        attr='parent_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='parent', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='rec', ctx=Load()),
                                                attr='_get_external_ids',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        slice=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='xxx.child', kind=None)],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='parent_id',
                                                    ctx=Load(),
                                                ),
                                                attr='_get_external_ids',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        slice=Attribute(
                                            value=Attribute(
                                                value=Name(id='rec', ctx=Load()),
                                                attr='parent_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
                                    Constant(value='no xid should be created for the parent', kind=None),
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
                    name='test_create_parent_with_xid',
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
                            targets=[Name(id='parent', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='export.inherits.parent', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='value_parent', kind=None)],
                                        values=[Constant(value=0, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pid', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.data', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='model', kind=None),
                                            Constant(value='res_id', kind=None),
                                            Constant(value='module', kind=None),
                                            Constant(value='name', kind=None),
                                        ],
                                        values=[
                                            Constant(value='export.inherits.parent', kind=None),
                                            Attribute(
                                                value=Name(id='parent', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='xxx', kind=None),
                                            Constant(value='parent', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='parent_id/.id', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='xxx.child', kind=None),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='parent', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='1', kind=None),
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
                        Assign(
                            targets=[Name(id='rec', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='model_name',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='r', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='rec', ctx=Load()),
                                        attr='value_parent',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='rec', ctx=Load()),
                                        attr='parent_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='parent', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='pid', ctx=Load()),
                                                attr='exists',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='res_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='parent', ctx=Load()),
                                        attr='id',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='rec', ctx=Load()),
                                                attr='_get_external_ids',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        slice=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='xxx.child', kind=None)],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='parent_id',
                                                    ctx=Load(),
                                                ),
                                                attr='_get_external_ids',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        slice=Attribute(
                                            value=Attribute(
                                                value=Name(id='rec', ctx=Load()),
                                                attr='parent_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='xxx.parent', kind=None)],
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
                    name='test_create_parent_by_xid',
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
                            targets=[Name(id='parent', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='export.inherits.parent', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='value_parent', kind=None)],
                                        values=[Constant(value=0, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pid', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.data', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='model', kind=None),
                                            Constant(value='res_id', kind=None),
                                            Constant(value='module', kind=None),
                                            Constant(value='name', kind=None),
                                        ],
                                        values=[
                                            Constant(value='export.inherits.parent', kind=None),
                                            Attribute(
                                                value=Name(id='parent', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='xxx', kind=None),
                                            Constant(value='parent', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='parent_id/id', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='xxx.child', kind=None),
                                                    Constant(value='xxx.parent', kind=None),
                                                    Constant(value='1', kind=None),
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
                        Assign(
                            targets=[Name(id='rec', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='model_name',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='r', ctx=Load()),
                                        slice=Constant(value='ids', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='rec', ctx=Load()),
                                        attr='value_parent',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='rec', ctx=Load()),
                                        attr='parent_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='parent', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='pid', ctx=Load()),
                                                attr='exists',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='res_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='parent', ctx=Load()),
                                        attr='id',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='rec', ctx=Load()),
                                                attr='_get_external_ids',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        slice=Attribute(
                                            value=Name(id='rec', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='xxx.child', kind=None)],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='rec', ctx=Load()),
                                                    attr='parent_id',
                                                    ctx=Load(),
                                                ),
                                                attr='_get_external_ids',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        slice=Attribute(
                                            value=Attribute(
                                                value=Name(id='rec', ctx=Load()),
                                                attr='parent_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='xxx.parent', kind=None)],
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
                    name='test_update_parent_no_xid',
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
                            targets=[Name(id='parent', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='export.inherits.parent', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='value_parent', kind=None)],
                                        values=[Constant(value=0, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='child', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='model_name',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='parent_id', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='parent', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1, kind=None),
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.data', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='model', kind=None),
                                            Constant(value='res_id', kind=None),
                                            Constant(value='module', kind=None),
                                            Constant(value='name', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='model_name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='child', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='xxx', kind=None),
                                            Constant(value='child', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='xxx.child', kind=None),
                                                    Constant(value='42', kind=None),
                                                ],
                                                ctx=Load(),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='child', ctx=Load()),
                                        attr='value',
                                        ctx=Load(),
                                    ),
                                    Constant(value=42, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='child', ctx=Load()),
                                        attr='parent_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='parent', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='child', ctx=Load()),
                                                attr='_get_external_ids',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        slice=Attribute(
                                            value=Name(id='child', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='xxx.child', kind=None)],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='parent', ctx=Load()),
                                                attr='_get_external_ids',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        slice=Attribute(
                                            value=Name(id='parent', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
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
                    name='test_update_parent_with_xid',
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
                            targets=[Name(id='parent', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='export.inherits.parent', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='value_parent', kind=None)],
                                        values=[Constant(value=0, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='child', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='model_name',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='parent_id', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='parent', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1, kind=None),
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
                                        Name(id='pid', ctx=Store()),
                                        Name(id='cid', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.data', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='model', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='module', kind=None),
                                                    Constant(value='name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='export.inherits.parent', kind=None),
                                                    Attribute(
                                                        value=Name(id='parent', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='xxx', kind=None),
                                                    Constant(value='parent', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='model', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='module', kind=None),
                                                    Constant(value='name', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='model_name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='child', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='xxx', kind=None),
                                                    Constant(value='child', kind=None),
                                                ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='import_',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='xxx.child', kind=None),
                                                    Constant(value='42', kind=None),
                                                ],
                                                ctx=Load(),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='child', ctx=Load()),
                                        attr='value',
                                        ctx=Load(),
                                    ),
                                    Constant(value=42, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='child', ctx=Load()),
                                        attr='parent_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='parent', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='pid', ctx=Load()),
                                                attr='exists',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='res_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='parent', ctx=Load()),
                                        attr='id',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='cid', ctx=Load()),
                                                attr='exists',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='res_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='child', ctx=Load()),
                                        attr='id',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='child', ctx=Load()),
                                                attr='_get_external_ids',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        slice=Attribute(
                                            value=Name(id='child', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='xxx.child', kind=None)],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='parent', ctx=Load()),
                                                attr='_get_external_ids',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        slice=Attribute(
                                            value=Name(id='parent', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='xxx.parent', kind=None)],
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
    ],
    type_ignores=[],
)
