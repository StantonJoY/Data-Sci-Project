Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='goal_manual_wizard',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Wizard to update a manual goal', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='gamification.goal.wizard', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Gamification Goal Wizard', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='goal_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='gamification.goal', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Goal', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='current', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Current', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_update_current',
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
                            value=Constant(value='Wizard action for updating the current value', kind=None),
                        ),
                        For(
                            target=Name(id='wiz', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='wiz', ctx=Load()),
                                                attr='goal_id',
                                                ctx=Load(),
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='current', kind=None),
                                                    Constant(value='goal_id', kind=None),
                                                    Constant(value='to_update', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='wiz', ctx=Load()),
                                                        attr='current',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='wiz', ctx=Load()),
                                                            attr='goal_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='wiz', ctx=Load()),
                                                attr='goal_id',
                                                ctx=Load(),
                                            ),
                                            attr='update_goal',
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
                        Return(
                            value=Constant(value=False, kind=None),
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
