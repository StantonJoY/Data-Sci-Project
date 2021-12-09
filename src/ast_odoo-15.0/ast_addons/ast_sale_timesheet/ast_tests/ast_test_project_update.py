Module(
    body=[
        ImportFrom(
            module='freezegun',
            names=[alias(name='freeze_time', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.project.tests.test_project_update_flow',
            names=[alias(name='TestProjectUpdate', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestProjectUpdateSaleTimesheet',
            bases=[Name(id='TestProjectUpdate', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_project_update_description_profitability',
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
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_pigs',
                                        ctx=Load(),
                                    ),
                                    attr='allow_billable',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='template_values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='project.update', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get_template_values',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_pigs',
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
                                        value=Subscript(
                                            value=Name(id='template_values', ctx=Load()),
                                            slice=Constant(value='profitability', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='costs', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='$\xa00.00', kind=None),
                                    Constant(value='Project costs used in the template should be well defined', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='template_values', ctx=Load()),
                                            slice=Constant(value='profitability', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='revenues', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='$\xa00.00', kind=None),
                                    Constant(value='Project revenues used in the template should be well defined', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='template_values', ctx=Load()),
                                            slice=Constant(value='profitability', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='margin', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='Margin used in the template should be well defined', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='template_values', ctx=Load()),
                                            slice=Constant(value='profitability', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='margin_formatted', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='$\xa00.00', kind=None),
                                    Constant(value='Margin formatted used in the template should be well defined', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='template_values', ctx=Load()),
                                            slice=Constant(value='profitability', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='margin_percentage', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='0', kind=None),
                                    Constant(value='Margin percentage used in the template should be well defined', kind=None),
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
                    name='test_project_update_panel_profitability_no_billable',
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
                            targets=[Name(id='panel_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='project_pigs',
                                        ctx=Load(),
                                    ),
                                    attr='get_panel_data',
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
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='panel_data', ctx=Load()),
                                            slice=Constant(value='profitability_items', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='allow_billable', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                    Constant(value='Project should not be billable by default', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='project_pigs',
                                                ctx=Load(),
                                            ),
                                            attr='action_view_timesheet',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='e',
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='AssertionError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='Error raised unexpectedly while calling the action defined in profitalities action panel data ! Exception : ', kind=None),
                                                        op=Add(),
                                                        right=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='e', ctx=Load()),
                                                                attr='args',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='project_pigs',
                                                ctx=Load(),
                                            ),
                                            attr='action_view_timesheet',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='e',
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='AssertionError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='Error raised unexpectedly while calling the action defined in profitalities action panel data ! Exception : ', kind=None),
                                                        op=Add(),
                                                        right=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='e', ctx=Load()),
                                                                attr='args',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
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
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='-at_install', kind=None),
                        Constant(value='post_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
