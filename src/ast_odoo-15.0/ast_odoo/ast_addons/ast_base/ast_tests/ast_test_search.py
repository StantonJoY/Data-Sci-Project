Module(
    body=[
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='Command', asname=None)],
            level=0,
        ),
        ClassDef(
            name='test_search',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='patch_order',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='patch',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='registry',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='model', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    Constant(value='_order', kind=None),
                                    Name(id='order', ctx=Load()),
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
                    name='test_00_search_order',
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
                            targets=[Name(id='Partner', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.partner', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='c', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Partner', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='test_search_order_C', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='d', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Partner', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='active', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_search_order_D', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='a', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Partner', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='test_search_order_A', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='b', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Partner', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='test_search_order_B', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ab', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Partner', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='test_search_order_AB', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='e', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Partner', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='active', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_search_order_E', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='name_asc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Partner', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='like', kind=None),
                                                    Constant(value='test_search_order%', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='name asc', kind=None),
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
                                    List(
                                        elts=[
                                            Name(id='a', ctx=Load()),
                                            Name(id='ab', ctx=Load()),
                                            Name(id='b', ctx=Load()),
                                            Name(id='c', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[Name(id='name_asc', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value="Search with 'NAME ASC' order failed.", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='name_desc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Partner', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='like', kind=None),
                                                    Constant(value='test_search_order%', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='name desc', kind=None),
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
                                    List(
                                        elts=[
                                            Name(id='c', ctx=Load()),
                                            Name(id='b', ctx=Load()),
                                            Name(id='ab', ctx=Load()),
                                            Name(id='a', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[Name(id='name_desc', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value="Search with 'NAME DESC' order failed.", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='id_asc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Partner', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='like', kind=None),
                                                    Constant(value='test_search_order%', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='id asc', kind=None),
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
                                    List(
                                        elts=[
                                            Name(id='c', ctx=Load()),
                                            Name(id='a', ctx=Load()),
                                            Name(id='b', ctx=Load()),
                                            Name(id='ab', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[Name(id='id_asc', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value="Search with 'ID ASC' order failed.", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='id_desc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Partner', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='like', kind=None),
                                                    Constant(value='test_search_order%', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='id desc', kind=None),
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
                                    List(
                                        elts=[
                                            Name(id='ab', ctx=Load()),
                                            Name(id='b', ctx=Load()),
                                            Name(id='a', ctx=Load()),
                                            Name(id='c', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[Name(id='id_desc', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value="Search with 'ID DESC' order failed.", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='active_asc_id_asc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Partner', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='like', kind=None),
                                                    Constant(value='test_search_order%', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='|', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='active asc, id asc', kind=None),
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
                                    List(
                                        elts=[
                                            Name(id='d', ctx=Load()),
                                            Name(id='e', ctx=Load()),
                                            Name(id='c', ctx=Load()),
                                            Name(id='a', ctx=Load()),
                                            Name(id='b', ctx=Load()),
                                            Name(id='ab', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[Name(id='active_asc_id_asc', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value="Search with 'ACTIVE ASC, ID ASC' order failed.", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='active_desc_id_asc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Partner', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='like', kind=None),
                                                    Constant(value='test_search_order%', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='|', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='active desc, id asc', kind=None),
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
                                    List(
                                        elts=[
                                            Name(id='c', ctx=Load()),
                                            Name(id='a', ctx=Load()),
                                            Name(id='b', ctx=Load()),
                                            Name(id='ab', ctx=Load()),
                                            Name(id='d', ctx=Load()),
                                            Name(id='e', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[Name(id='active_desc_id_asc', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value="Search with 'ACTIVE DESC, ID ASC' order failed.", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='active_asc_id_desc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Partner', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='like', kind=None),
                                                    Constant(value='test_search_order%', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='|', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='active asc, id desc', kind=None),
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
                                    List(
                                        elts=[
                                            Name(id='e', ctx=Load()),
                                            Name(id='d', ctx=Load()),
                                            Name(id='ab', ctx=Load()),
                                            Name(id='b', ctx=Load()),
                                            Name(id='a', ctx=Load()),
                                            Name(id='c', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[Name(id='active_asc_id_desc', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value="Search with 'ACTIVE ASC, ID DESC' order failed.", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='active_desc_id_desc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Partner', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='like', kind=None),
                                                    Constant(value='test_search_order%', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='|', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='active desc, id desc', kind=None),
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
                                    List(
                                        elts=[
                                            Name(id='ab', ctx=Load()),
                                            Name(id='b', ctx=Load()),
                                            Name(id='a', ctx=Load()),
                                            Name(id='c', ctx=Load()),
                                            Name(id='e', ctx=Load()),
                                            Name(id='d', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[Name(id='active_desc_id_desc', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value="Search with 'ACTIVE DESC, ID DESC' order failed.", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='id_asc_active_asc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Partner', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='like', kind=None),
                                                    Constant(value='test_search_order%', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='|', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='id asc, active asc', kind=None),
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
                                    List(
                                        elts=[
                                            Name(id='c', ctx=Load()),
                                            Name(id='d', ctx=Load()),
                                            Name(id='a', ctx=Load()),
                                            Name(id='b', ctx=Load()),
                                            Name(id='ab', ctx=Load()),
                                            Name(id='e', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[Name(id='id_asc_active_asc', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value="Search with 'ID ASC, ACTIVE ASC' order failed.", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='id_asc_active_desc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Partner', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='like', kind=None),
                                                    Constant(value='test_search_order%', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='|', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='id asc, active desc', kind=None),
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
                                    List(
                                        elts=[
                                            Name(id='c', ctx=Load()),
                                            Name(id='d', ctx=Load()),
                                            Name(id='a', ctx=Load()),
                                            Name(id='b', ctx=Load()),
                                            Name(id='ab', ctx=Load()),
                                            Name(id='e', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[Name(id='id_asc_active_desc', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value="Search with 'ID ASC, ACTIVE DESC' order failed.", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='id_desc_active_asc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Partner', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='like', kind=None),
                                                    Constant(value='test_search_order%', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='|', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='id desc, active asc', kind=None),
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
                                    List(
                                        elts=[
                                            Name(id='e', ctx=Load()),
                                            Name(id='ab', ctx=Load()),
                                            Name(id='b', ctx=Load()),
                                            Name(id='a', ctx=Load()),
                                            Name(id='d', ctx=Load()),
                                            Name(id='c', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[Name(id='id_desc_active_asc', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value="Search with 'ID DESC, ACTIVE ASC' order failed.", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='id_desc_active_desc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Partner', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='like', kind=None),
                                                    Constant(value='test_search_order%', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='|', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='id desc, active desc', kind=None),
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
                                    List(
                                        elts=[
                                            Name(id='e', ctx=Load()),
                                            Name(id='ab', ctx=Load()),
                                            Name(id='b', ctx=Load()),
                                            Name(id='a', ctx=Load()),
                                            Name(id='d', ctx=Load()),
                                            Name(id='c', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[Name(id='id_desc_active_desc', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value="Search with 'ID DESC, ACTIVE DESC' order failed.", kind=None),
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
                    name='test_10_inherits_m2order',
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
                            targets=[Name(id='Users', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.users', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='group_employee', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.group_user', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='country_be', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.be', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='country_us', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.us', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='states_us', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='country_us', ctx=Load()),
                                    attr='state_ids',
                                    ctx=Load(),
                                ),
                                slice=Slice(
                                    lower=None,
                                    upper=Constant(value=2, kind=None),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='u', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Users', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                            Constant(value='groups_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='__search', kind=None),
                                            Constant(value='__search', kind=None),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='set',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Name(id='group_employee', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='a', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Users', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                            Constant(value='country_id', kind=None),
                                            Constant(value='state_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='__test_A', kind=None),
                                            Constant(value='__test_A', kind=None),
                                            Attribute(
                                                value=Name(id='country_be', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='country_be', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='b', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Users', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                            Constant(value='country_id', kind=None),
                                            Constant(value='state_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='__test_B', kind=None),
                                            Constant(value='__a_test_B', kind=None),
                                            Attribute(
                                                value=Name(id='country_us', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='states_us', ctx=Load()),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='c', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Users', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                            Constant(value='country_id', kind=None),
                                            Constant(value='state_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='__test_B', kind=None),
                                            Constant(value='__z_test_B', kind=None),
                                            Attribute(
                                                value=Name(id='country_us', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='states_us', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Users', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Users', ctx=Load()),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[Name(id='u', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_ids', ctx=Store())],
                            value=List(
                                elts=[
                                    Attribute(
                                        value=Name(id='u', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='a', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='c', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='b', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user_ids', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='Users', ctx=Load()),
                                        attr='search',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Name(id='expected_ids', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='order',
                                            value=Constant(value='name asc, login desc', kind=None),
                                        ),
                                    ],
                                ),
                                attr='ids',
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
                                    Name(id='user_ids', ctx=Load()),
                                    Name(id='expected_ids', ctx=Load()),
                                    Constant(value='search on res_users did not provide expected ids or expected order', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected_ids', ctx=Store())],
                            value=List(
                                elts=[
                                    Attribute(
                                        value=Name(id='c', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='b', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='a', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='u', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user_ids', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='Users', ctx=Load()),
                                        attr='search',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Name(id='expected_ids', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='order',
                                            value=Constant(value='state_id asc, country_id desc, name asc, login desc', kind=None),
                                        ),
                                    ],
                                ),
                                attr='ids',
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
                                    Name(id='user_ids', ctx=Load()),
                                    Name(id='expected_ids', ctx=Load()),
                                    Constant(value='search on res_users did not provide expected ids or expected order', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected_ids', ctx=Store())],
                            value=List(
                                elts=[
                                    Attribute(
                                        value=Name(id='u', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='b', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='c', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='a', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user_ids', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='Users', ctx=Load()),
                                        attr='search',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Name(id='expected_ids', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='order',
                                            value=Constant(value='country_id desc, state_id desc, name asc, login desc', kind=None),
                                        ),
                                    ],
                                ),
                                attr='ids',
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
                                    Name(id='user_ids', ctx=Load()),
                                    Name(id='expected_ids', ctx=Load()),
                                    Constant(value='search on res_users did not provide expected ids or expected order', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='patch_order',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='res.users', kind=None),
                                    Constant(value='country_id desc, name asc, login desc', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected_ids', ctx=Store())],
                            value=List(
                                elts=[
                                    Attribute(
                                        value=Name(id='u', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='c', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='b', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='a', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user_ids', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='Users', ctx=Load()),
                                        attr='search',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Name(id='expected_ids', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='ids',
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
                                    Name(id='user_ids', ctx=Load()),
                                    Name(id='expected_ids', ctx=Load()),
                                    Constant(value='search on res_users did not provide expected ids or expected order', kind=None),
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
                    name='test_11_indirect_inherits_m2o_order',
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
                            targets=[Name(id='Cron', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.cron', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Users', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.users', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user_ids', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cron_ids', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='u', ctx=Store()),
                            iter=Constant(value='BAC', kind=None),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='user_ids', ctx=Load()),
                                            slice=Name(id='u', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='Users', ctx=Load()),
                                                attr='create',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Dict(
                                                    keys=[
                                                        Constant(value='name', kind=None),
                                                        Constant(value='login', kind=None),
                                                    ],
                                                    values=[
                                                        Name(id='u', ctx=Load()),
                                                        Name(id='u', ctx=Load()),
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
                                    targets=[
                                        Subscript(
                                            value=Name(id='cron_ids', ctx=Load()),
                                            slice=Name(id='u', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='Cron', ctx=Load()),
                                                attr='create',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Dict(
                                                    keys=[
                                                        Constant(value='name', kind=None),
                                                        Constant(value='model_id', kind=None),
                                                        Constant(value='user_id', kind=None),
                                                    ],
                                                    values=[
                                                        Name(id='u', ctx=Load()),
                                                        Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='ref',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='base.model_res_partner', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        Subscript(
                                                            value=Name(id='user_ids', ctx=Load()),
                                                            slice=Name(id='u', ctx=Load()),
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
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ids', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='Cron', ctx=Load()),
                                        attr='search',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Call(
                                                            func=Name(id='list', ctx=Load()),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='cron_ids', ctx=Load()),
                                                                        attr='values',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
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
                                    keywords=[
                                        keyword(
                                            arg='order',
                                            value=Constant(value='user_id', kind=None),
                                        ),
                                    ],
                                ),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_ids', ctx=Store())],
                            value=ListComp(
                                elt=Subscript(
                                    value=Name(id='cron_ids', ctx=Load()),
                                    slice=Name(id='l', ctx=Load()),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='l', ctx=Store()),
                                        iter=Constant(value='ABC', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='ids', ctx=Load()),
                                    Name(id='expected_ids', ctx=Load()),
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
                    name='test_12_m2o_order_loop_self',
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
                            targets=[Name(id='Cats', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.module.category', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cat_ids', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='create',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='name', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kw', annotation=None, type_comment=None),
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='cat_ids', ctx=Load()),
                                            slice=Name(id='name', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='Cats', ctx=Load()),
                                                attr='create',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Name(id='dict', ctx=Load()),
                                                    args=[Name(id='kw', ctx=Load())],
                                                    keywords=[
                                                        keyword(
                                                            arg='name',
                                                            value=Name(id='name', ctx=Load()),
                                                        ),
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
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='patch_order',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ir.module.category', kind=None),
                                    Constant(value='parent_id desc, name', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='create', ctx=Load()),
                                args=[Constant(value='A', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='create', ctx=Load()),
                                args=[Constant(value='B', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='parent_id',
                                        value=Subscript(
                                            value=Name(id='cat_ids', ctx=Load()),
                                            slice=Constant(value='A', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='create', ctx=Load()),
                                args=[Constant(value='C', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='parent_id',
                                        value=Subscript(
                                            value=Name(id='cat_ids', ctx=Load()),
                                            slice=Constant(value='A', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='create', ctx=Load()),
                                args=[Constant(value='D', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='create', ctx=Load()),
                                args=[Constant(value='E', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='parent_id',
                                        value=Subscript(
                                            value=Name(id='cat_ids', ctx=Load()),
                                            slice=Constant(value='D', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='create', ctx=Load()),
                                args=[Constant(value='F', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='parent_id',
                                        value=Subscript(
                                            value=Name(id='cat_ids', ctx=Load()),
                                            slice=Constant(value='D', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected_ids', ctx=Store())],
                            value=ListComp(
                                elt=Subscript(
                                    value=Name(id='cat_ids', ctx=Load()),
                                    slice=Name(id='x', ctx=Load()),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='x', ctx=Store()),
                                        iter=Constant(value='ADEFBC', kind=None),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='found_ids', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='Cats', ctx=Load()),
                                        attr='search',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Call(
                                                            func=Name(id='list', ctx=Load()),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='cat_ids', ctx=Load()),
                                                                        attr='values',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
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
                                attr='ids',
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
                                    Name(id='found_ids', ctx=Load()),
                                    Name(id='expected_ids', ctx=Load()),
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
                    name='test_13_m2o_order_loop_multi',
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
                            targets=[Name(id='Users', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.users', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='patch_order',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='res.partner', kind=None),
                                    Constant(value='create_uid, name', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='patch_order',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='res.users', kind=None),
                                    Constant(value='partner_id, login desc', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='kw', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='groups_id',
                                        value=List(
                                            elts=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='Command', ctx=Load()),
                                                        attr='set',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        List(
                                                            elts=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='ref',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='base.group_system', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='ref',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='base.group_partner_manager', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='u1', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='Users', ctx=Load()),
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='name',
                                                    value=Constant(value='Q', kind=None),
                                                ),
                                                keyword(
                                                    arg='login',
                                                    value=Constant(value='m', kind=None),
                                                ),
                                                keyword(
                                                    arg=None,
                                                    value=Name(id='kw', ctx=Load()),
                                                ),
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
                            targets=[Name(id='u2', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='Users', ctx=Load()),
                                                attr='with_user',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='u1', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='name',
                                                    value=Constant(value='B', kind=None),
                                                ),
                                                keyword(
                                                    arg='login',
                                                    value=Constant(value='f', kind=None),
                                                ),
                                                keyword(
                                                    arg=None,
                                                    value=Name(id='kw', ctx=Load()),
                                                ),
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
                            targets=[Name(id='u3', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='Users', ctx=Load()),
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='name',
                                                    value=Constant(value='C', kind=None),
                                                ),
                                                keyword(
                                                    arg='login',
                                                    value=Constant(value='c', kind=None),
                                                ),
                                                keyword(
                                                    arg=None,
                                                    value=Name(id='kw', ctx=Load()),
                                                ),
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
                            targets=[Name(id='u4', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='Users', ctx=Load()),
                                                attr='with_user',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='u2', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='name',
                                                    value=Constant(value='D', kind=None),
                                                ),
                                                keyword(
                                                    arg='login',
                                                    value=Constant(value='z', kind=None),
                                                ),
                                                keyword(
                                                    arg=None,
                                                    value=Name(id='kw', ctx=Load()),
                                                ),
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
                            targets=[Name(id='expected_ids', ctx=Store())],
                            value=List(
                                elts=[
                                    Name(id='u2', ctx=Load()),
                                    Name(id='u4', ctx=Load()),
                                    Name(id='u3', ctx=Load()),
                                    Name(id='u1', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='found_ids', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='Users', ctx=Load()),
                                        attr='search',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        Name(id='expected_ids', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='ids',
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
                                    Name(id='found_ids', ctx=Load()),
                                    Name(id='expected_ids', ctx=Load()),
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
                    name='test_20_x_active',
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
                            value=Constant(value='Check the behaviour of the x_active field.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='model_country', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.country', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='active', kind=None),
                                    Attribute(
                                        value=Name(id='model_country', ctx=Load()),
                                        attr='_fields',
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
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.fields', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='model_id', kind=None),
                                            Constant(value='ttype', kind=None),
                                        ],
                                        values=[
                                            Constant(value='x_active', kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ref',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='base.model_res_country', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='boolean', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='x_active', kind=None),
                                    Attribute(
                                        value=Name(id='model_country', ctx=Load()),
                                        attr='_active_name',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='country_ussr', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model_country', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='x_active', kind=None),
                                        ],
                                        values=[
                                            Constant(value='USSR', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ussr_search', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model_country', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='USSR', kind=None),
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
                                args=[Name(id='ussr_search', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='ussr_search', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='model_country', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='active_test',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='USSR', kind=None),
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
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='country_ussr', ctx=Load()),
                                    Name(id='ussr_search', ctx=Load()),
                                    Constant(value='Search with active_test on a custom x_active field failed', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='ussr_search', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model_country', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='USSR', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='x_active', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
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
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='country_ussr', ctx=Load()),
                                    Name(id='ussr_search', ctx=Load()),
                                    Constant(value='Search with active_test on a custom x_active field failed', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='model_bank', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.bank', kind=None),
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
                                        slice=Constant(value='ir.model.fields', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='model_id', kind=None),
                                            Constant(value='ttype', kind=None),
                                        ],
                                        values=[
                                            Constant(value='x_active', kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ref',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='base.model_res_bank', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='boolean', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='active', kind=None),
                                    Attribute(
                                        value=Name(id='model_bank', ctx=Load()),
                                        attr='_active_name',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='bank_credit_communal', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model_bank', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='x_active', kind=None),
                                            Constant(value='active', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Crédit Communal', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cc_search', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model_bank', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='Crédit Communal', kind=None),
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
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='bank_credit_communal', ctx=Load()),
                                    Name(id='cc_search', ctx=Load()),
                                    Constant(value='Search for active record with x_active set to False has failed', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='bank_credit_communal', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='active', kind=None),
                                            Constant(value='x_active', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='cc_search', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model_bank', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='Crédit Communal', kind=None),
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
                                    attr='assertNotIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='bank_credit_communal', ctx=Load()),
                                    Name(id='cc_search', ctx=Load()),
                                    Constant(value='Search for inactive record with x_active set to True has failed', kind=None),
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
