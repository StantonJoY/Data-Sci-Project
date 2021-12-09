Module(
    body=[
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='standalone', asname=None)],
            level=0,
        ),
        FunctionDef(
            name='test_01_cow_views_unlink_on_module_update',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='env', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Ensure COW views are correctly removed during module update.\n    Not removing the view could lead to traceback:\n    - Having a view A\n    - Having a view B that inherits from a view C\n    - View B t-call view A\n    - COW view B\n    - Delete view A and B from module datas and update it\n    - Rendering view C will crash since it will render child view B that\n      t-call unexisting view A\n    ', kind=None),
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
                Assign(
                    targets=[Name(id='Imd', ctx=Store())],
                    value=Subscript(
                        value=Name(id='env', ctx=Load()),
                        slice=Constant(value='ir.model.data', kind=None),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='update_module_base_view', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='env', ctx=Load()),
                            attr='ref',
                            ctx=Load(),
                        ),
                        args=[Constant(value='test_website.update_module_base_view', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='update_module_view_to_be_t_called', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='View', ctx=Load()),
                            attr='create',
                            ctx=Load(),
                        ),
                        args=[
                            Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='arch', kind=None),
                                    Constant(value='key', kind=None),
                                ],
                                values=[
                                    Constant(value='View to be t-called', kind=None),
                                    Constant(value='qweb', kind=None),
                                    Constant(value='<div>I will be t-called</div>', kind=None),
                                    Constant(value='test_website.update_module_view_to_be_t_called', kind=None),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='update_module_child_view', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='View', ctx=Load()),
                            attr='create',
                            ctx=Load(),
                        ),
                        args=[
                            Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='mode', kind=None),
                                    Constant(value='inherit_id', kind=None),
                                    Constant(value='arch', kind=None),
                                    Constant(value='key', kind=None),
                                ],
                                values=[
                                    Constant(value='Child View', kind=None),
                                    Constant(value='extension', kind=None),
                                    Attribute(
                                        value=Name(id='update_module_base_view', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='\n            <div position="inside">\n                <t t-call="test_website.update_module_view_to_be_t_called"/>\n            </div>\n        ', kind=None),
                                    Constant(value='test_website.update_module_child_view', kind=None),
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
                            value=Name(id='Imd', ctx=Load()),
                            attr='create',
                            ctx=Load(),
                        ),
                        args=[
                            Dict(
                                keys=[
                                    Constant(value='module', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='model', kind=None),
                                    Constant(value='res_id', kind=None),
                                ],
                                values=[
                                    Constant(value='test_website', kind=None),
                                    Constant(value='update_module_view_to_be_t_called', kind=None),
                                    Constant(value='ir.ui.view', kind=None),
                                    Attribute(
                                        value=Name(id='update_module_view_to_be_t_called', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
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
                            value=Name(id='Imd', ctx=Load()),
                            attr='create',
                            ctx=Load(),
                        ),
                        args=[
                            Dict(
                                keys=[
                                    Constant(value='module', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='model', kind=None),
                                    Constant(value='res_id', kind=None),
                                ],
                                values=[
                                    Constant(value='test_website', kind=None),
                                    Constant(value='update_module_child_view', kind=None),
                                    Constant(value='ir.ui.view', kind=None),
                                    Attribute(
                                        value=Name(id='update_module_child_view', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='update_module_child_view', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='website_id',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            attr='write',
                            ctx=Load(),
                        ),
                        args=[
                            Dict(
                                keys=[Constant(value='name', kind=None)],
                                values=[Constant(value='Child View (W1)', kind=None)],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='msg', ctx=Store())],
                    value=Constant(value="View '%s' does not exist!", kind=None),
                    type_comment=None,
                ),
                Assert(
                    test=Compare(
                        left=Call(
                            func=Attribute(
                                value=Name(id='View', ctx=Load()),
                                attr='search_count',
                                ctx=Load(),
                            ),
                            args=[
                                List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='type', kind=None),
                                                Constant(value='=', kind=None),
                                                Constant(value='qweb', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='key', kind=None),
                                                Constant(value='=', kind=None),
                                                Attribute(
                                                    value=Name(id='update_module_child_view', ctx=Load()),
                                                    attr='key',
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
                        ops=[Eq()],
                        comparators=[Constant(value=2, kind=None)],
                    ),
                    msg=BinOp(
                        left=Name(id='msg', ctx=Load()),
                        op=Mod(),
                        right=Attribute(
                            value=Name(id='update_module_child_view', ctx=Load()),
                            attr='key',
                            ctx=Load(),
                        ),
                    ),
                ),
                Assert(
                    test=Call(
                        func=Name(id='bool', ctx=Load()),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='env', ctx=Load()),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='update_module_view_to_be_t_called', ctx=Load()),
                                        attr='key',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                    msg=BinOp(
                        left=Name(id='msg', ctx=Load()),
                        op=Mod(),
                        right=Attribute(
                            value=Name(id='update_module_view_to_be_t_called', ctx=Load()),
                            attr='key',
                            ctx=Load(),
                        ),
                    ),
                ),
                Assert(
                    test=Call(
                        func=Name(id='bool', ctx=Load()),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='env', ctx=Load()),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='update_module_base_view', ctx=Load()),
                                        attr='key',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                    msg=BinOp(
                        left=Name(id='msg', ctx=Load()),
                        op=Mod(),
                        right=Attribute(
                            value=Name(id='update_module_base_view', ctx=Load()),
                            attr='key',
                            ctx=Load(),
                        ),
                    ),
                ),
                Assign(
                    targets=[Name(id='test_website_module', ctx=Store())],
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
                                            Constant(value='name', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value='test_website', kind=None),
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
                            value=Name(id='test_website_module', ctx=Load()),
                            attr='button_immediate_upgrade',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='env', ctx=Load()),
                            attr='reset',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='env', ctx=Store())],
                    value=Call(
                        func=Name(id='env', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='view', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='env', ctx=Load()),
                            attr='ref',
                            ctx=Load(),
                        ),
                        args=[Constant(value='test_website.update_module_view_to_be_t_called', kind=None)],
                        keywords=[
                            keyword(
                                arg='raise_if_not_found',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assert(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='view', ctx=Load()),
                    ),
                    msg=Constant(value='Generic view did not get removed!', kind=None),
                ),
                Assert(
                    test=UnaryOp(
                        op=Not(),
                        operand=Call(
                            func=Attribute(
                                value=Subscript(
                                    value=Name(id='env', ctx=Load()),
                                    slice=Constant(value='ir.ui.view', kind=None),
                                    ctx=Load(),
                                ),
                                attr='search_count',
                                ctx=Load(),
                            ),
                            args=[
                                List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='type', kind=None),
                                                Constant(value='=', kind=None),
                                                Constant(value='qweb', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='key', kind=None),
                                                Constant(value='=', kind=None),
                                                Constant(value='test_website.update_module_child_view', kind=None),
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
                    msg=Constant(value='Specific COW views did not get removed!', kind=None),
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='standalone', ctx=Load()),
                    args=[Constant(value='cow_views', kind=None)],
                    keywords=[],
                ),
            ],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
