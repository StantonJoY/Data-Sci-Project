Module(
    body=[
        Expr(
            value=Constant(value=' This test ensure `inherit_id` update is correctly replicated on cow views.\nThe view receiving the `inherit_id` update is either:\n1. in a module loaded before `website`. In that case, `website` code is not\n   loaded yet, so we store the updates to replay the changes on the cow views\n   once `website` module is loaded (see `_check()`). This test is testing that\n   part.\n2. in a module loaded after `website`. In that case, the `inherit_id` update is\n   directly replicated on the cow views. That behavior is tested with\n   `test_module_new_inherit_view_on_parent_already_forked` and\n   `test_specific_view_module_update_inherit_change` in `website` module.\n', kind=None),
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='standalone', asname=None)],
            level=0,
        ),
        FunctionDef(
            name='test_01_cow_views_inherit_on_module_update',
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
                Assign(
                    targets=[Name(id='View', ctx=Store())],
                    value=Subscript(
                        value=Name(id='env', ctx=Load()),
                        slice=Constant(value='ir.ui.view', kind=None),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='View', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='_force_unlink',
                                                value=Constant(value=True, kind=None),
                                            ),
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
                                                    Constant(value='website_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
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
                    targets=[Name(id='child_view', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='env', ctx=Load()),
                            attr='ref',
                            ctx=Load(),
                        ),
                        args=[Constant(value='portal.footer_language_selector', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='parent_view', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='env', ctx=Load()),
                            attr='ref',
                            ctx=Load(),
                        ),
                        args=[Constant(value='portal.portal_back_in_edit_mode', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='child_view', ctx=Load()),
                            attr='write',
                            ctx=Load(),
                        ),
                        args=[
                            Dict(
                                keys=[
                                    Constant(value='inherit_id', kind=None),
                                    Constant(value='arch', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='parent_view', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='child_view', ctx=Load()),
                                                attr='arch_db',
                                                ctx=Load(),
                                            ),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='o_footer_copyright_name', kind=None),
                                            Constant(value='text-center', kind=None),
                                        ],
                                        keywords=[],
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
                                    value=Name(id='child_view', ctx=Load()),
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
                                values=[Constant(value='COW Website 1', kind=None)],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='child_cow_view', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='child_view', ctx=Load()),
                            attr='_get_specific_views',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assert(
                    test=Compare(
                        left=Attribute(
                            value=Name(id='child_cow_view', ctx=Load()),
                            attr='inherit_id',
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Name(id='parent_view', ctx=Load())],
                    ),
                    msg=Constant(value='Ensure test is setup as expected.', kind=None),
                ),
                Assign(
                    targets=[Name(id='portal_module', ctx=Store())],
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
                                            Constant(value='portal', kind=None),
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
                            value=Name(id='portal_module', ctx=Load()),
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
                    targets=[Name(id='expected_parent_view', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='env', ctx=Load()),
                            attr='ref',
                            ctx=Load(),
                        ),
                        args=[Constant(value='portal.frontend_layout', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assert(
                    test=Compare(
                        left=Attribute(
                            value=Name(id='child_view', ctx=Load()),
                            attr='inherit_id',
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Name(id='expected_parent_view', ctx=Load())],
                    ),
                    msg=Constant(value='Generic view security check.', kind=None),
                ),
                Assert(
                    test=Compare(
                        left=Attribute(
                            value=Name(id='child_cow_view', ctx=Load()),
                            attr='inherit_id',
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Name(id='expected_parent_view', ctx=Load())],
                    ),
                    msg=Constant(value='COW view should also have received the `inherit_id` update.', kind=None),
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='standalone', ctx=Load()),
                    args=[Constant(value='cow_views_inherit', kind=None)],
                    keywords=[],
                ),
            ],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='test_02_cow_views_inherit_on_module_update',
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
                Assign(
                    targets=[Name(id='View', ctx=Store())],
                    value=Subscript(
                        value=Name(id='env', ctx=Load()),
                        slice=Constant(value='ir.ui.view', kind=None),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='View', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='_force_unlink',
                                                value=Constant(value=True, kind=None),
                                            ),
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
                                                    Constant(value='website_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
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
                    targets=[Name(id='view_D', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='env', ctx=Load()),
                            attr='ref',
                            ctx=Load(),
                        ),
                        args=[Constant(value='portal.my_account_link', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='view_A', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='env', ctx=Load()),
                            attr='ref',
                            ctx=Load(),
                        ),
                        args=[Constant(value='portal.message_thread', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='view_D', ctx=Load()),
                            attr='write',
                            ctx=Load(),
                        ),
                        args=[
                            Dict(
                                keys=[
                                    Constant(value='inherit_id', kind=None),
                                    Constant(value='arch_db', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='view_A', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='view_D', ctx=Load()),
                                                attr='arch_db',
                                                ctx=Load(),
                                            ),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='o_logout_divider', kind=None),
                                            Constant(value='discussion', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='view_B', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='env', ctx=Load()),
                            attr='ref',
                            ctx=Load(),
                        ),
                        args=[Constant(value='portal.user_dropdown', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='view_D', ctx=Load()),
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
                                values=[Constant(value='D Website 1', kind=None)],
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
                                    value=Name(id='view_B', ctx=Load()),
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
                                values=[Constant(value='B Website 1', kind=None)],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='view_Dcow', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='view_D', ctx=Load()),
                            attr='_get_specific_views',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='view_Bcow', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='view_B', ctx=Load()),
                            attr='_get_specific_views',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assert(
                    test=Compare(
                        left=Attribute(
                            value=Name(id='view_Dcow', ctx=Load()),
                            attr='inherit_id',
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Name(id='view_A', ctx=Load())],
                    ),
                    msg=Constant(value='Ensure test is setup as expected.', kind=None),
                ),
                Assert(
                    test=Compare(
                        left=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[Name(id='view_Bcow', ctx=Load())],
                            keywords=[],
                        ),
                        ops=[
                            Eq(),
                            Eq(),
                        ],
                        comparators=[
                            Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='view_Dcow', ctx=Load())],
                                keywords=[],
                            ),
                            Constant(value=1, kind=None),
                        ],
                    ),
                    msg=Constant(value='Ensure test is setup as expected (2).', kind=None),
                ),
                Assert(
                    test=Compare(
                        left=Name(id='view_B', ctx=Load()),
                        ops=[NotEq()],
                        comparators=[Name(id='view_Bcow', ctx=Load())],
                    ),
                    msg=Constant(value='Security check to ensure `_get_specific_views` return what it should.', kind=None),
                ),
                Assign(
                    targets=[Name(id='portal_module', ctx=Store())],
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
                                            Constant(value='portal', kind=None),
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
                            value=Name(id='portal_module', ctx=Load()),
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
                Assert(
                    test=Compare(
                        left=Attribute(
                            value=Name(id='view_D', ctx=Load()),
                            attr='inherit_id',
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Name(id='view_B', ctx=Load())],
                    ),
                    msg=Constant(value='Generic view security check.', kind=None),
                ),
                Assert(
                    test=Compare(
                        left=Attribute(
                            value=Name(id='view_Dcow', ctx=Load()),
                            attr='inherit_id',
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Name(id='view_Bcow', ctx=Load())],
                    ),
                    msg=Constant(value='COW view should also have received the `inherit_id` update.', kind=None),
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='standalone', ctx=Load()),
                    args=[Constant(value='cow_views_inherit', kind=None)],
                    keywords=[],
                ),
            ],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
