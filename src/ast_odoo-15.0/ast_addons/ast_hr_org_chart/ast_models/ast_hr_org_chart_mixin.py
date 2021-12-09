Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='HrEmployeeBase',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='hr.employee.base', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='child_all_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Indirect Subordinates Count', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_subordinates', kind=None),
                            ),
                            keyword(
                                arg='recursive',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='compute_sudo',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_subordinates',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='parents', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        Helper function to compute subordinates_ids.\n        Get all subordinates (direct and indirect) of an employee.\n        An employee can be a manager of his own manager (recursive hierarchy; e.g. the CEO is manager of everyone but is also\n        member of the RD department, managed by the CTO itself managed by the CEO).\n        In that case, the manager in not counted as a subordinate if it's in the 'parents' set.\n        ", kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='parents', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='parents', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_name',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='indirect_subordinates', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_name',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Name(id='parents', ctx=Store()),
                            op=BitOr(),
                            value=Name(id='self', ctx=Load()),
                        ),
                        Assign(
                            targets=[Name(id='direct_subordinates', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='child_ids',
                                    ctx=Load(),
                                ),
                                op=Sub(),
                                right=Name(id='parents', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='child', ctx=Store()),
                            iter=Name(id='direct_subordinates', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='child_subordinate', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='child', ctx=Load()),
                                            attr='_get_subordinates',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='parents',
                                                value=Name(id='parents', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='indirect_subordinates', ctx=Store()),
                                    op=BitOr(),
                                    value=Name(id='child_subordinate', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Name(id='indirect_subordinates', ctx=Load()),
                                op=BitOr(),
                                right=Name(id='direct_subordinates', ctx=Load()),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_subordinates',
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
                            target=Name(id='employee', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='employee', ctx=Load()),
                                            attr='subordinate_ids',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='employee', ctx=Load()),
                                            attr='_get_subordinates',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='employee', ctx=Load()),
                                            attr='child_all_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='employee', ctx=Load()),
                                                attr='subordinate_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='child_ids', kind=None),
                                Constant(value='child_ids.child_all_count', kind=None),
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
    ],
    type_ignores=[],
)
