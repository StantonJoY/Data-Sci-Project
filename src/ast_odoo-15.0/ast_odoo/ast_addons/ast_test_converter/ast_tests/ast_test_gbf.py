Module(
    body=[
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestGBF',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='TransactionCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_group_by_full',
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
                            targets=[Name(id='Sub', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='test_converter.test_model.sub', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='TM', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='test_converter.test_model', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Sub', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='subs_ids', ctx=Store())],
                            value=ListComp(
                                elt=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Sub', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='name', kind=None)],
                                                values=[
                                                    BinOp(
                                                        left=Constant(value='sub%d', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='i', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='i', ctx=Store()),
                                        iter=Call(
                                            func=Name(id='range', ctx=Load()),
                                            args=[Constant(value=5, kind=None)],
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
                            targets=[Name(id='tm_ids', ctx=Store())],
                            value=ListComp(
                                elt=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='TM', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='many2one', kind=None)],
                                                values=[
                                                    Subscript(
                                                        value=Name(id='subs_ids', ctx=Load()),
                                                        slice=Name(id='i', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='i', ctx=Store()),
                                        iter=Call(
                                            func=Name(id='range', ctx=Load()),
                                            args=[Constant(value=3, kind=None)],
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
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='in', kind=None),
                                            Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[Name(id='tm_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rg', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='TM', ctx=Load()),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[Constant(value='many2one', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='many2one', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='rg', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='subs_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='rg_subs', ctx=Store())],
                            value=Call(
                                func=Name(id='sorted', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Subscript(
                                            value=Subscript(
                                                value=Name(id='g', ctx=Load()),
                                                slice=Constant(value='many2one', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='g', ctx=Store()),
                                                iter=Name(id='rg', ctx=Load()),
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
                                    attr='assertListEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='rg_subs', ctx=Load()),
                                    Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[Name(id='subs_ids', ctx=Load())],
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
    ],
    type_ignores=[],
)
