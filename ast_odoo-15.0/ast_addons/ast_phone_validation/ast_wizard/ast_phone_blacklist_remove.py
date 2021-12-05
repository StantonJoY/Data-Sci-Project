Module(
    body=[
        ImportFrom(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=6,
            col_offset=0,
            end_lineno=14,
            end_col_offset=93,
            name='PhoneBlacklistRemove',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=27,
                    end_lineno=6,
                    end_col_offset=48,
                    value=Name(lineno=6, col_offset=27, end_lineno=6, end_col_offset=33, id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=7,
                    col_offset=4,
                    end_lineno=7,
                    end_col_offset=36,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=7, col_offset=12, end_lineno=7, end_col_offset=36, value='phone.blacklist.remove', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=48,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=8, col_offset=19, end_lineno=8, end_col_offset=48, value='Remove phone from blacklist', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=76,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=9, id='phone', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=12,
                        end_lineno=10,
                        end_col_offset=76,
                        func=Attribute(
                            lineno=10,
                            col_offset=12,
                            end_lineno=10,
                            end_col_offset=23,
                            value=Name(lineno=10, col_offset=12, end_lineno=10, end_col_offset=18, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=10,
                                col_offset=24,
                                end_lineno=10,
                                end_col_offset=45,
                                arg='string',
                                value=Constant(lineno=10, col_offset=31, end_lineno=10, end_col_offset=45, value='Phone Number', kind=None),
                            ),
                            keyword(
                                lineno=10,
                                col_offset=47,
                                end_lineno=10,
                                end_col_offset=60,
                                arg='readonly',
                                value=Constant(lineno=10, col_offset=56, end_lineno=10, end_col_offset=60, value=True, kind=None),
                            ),
                            keyword(
                                lineno=10,
                                col_offset=62,
                                end_lineno=10,
                                end_col_offset=75,
                                arg='required',
                                value=Constant(lineno=10, col_offset=71, end_lineno=10, end_col_offset=75, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=39,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=10, id='reason', ctx=Store())],
                    value=Call(
                        lineno=11,
                        col_offset=13,
                        end_lineno=11,
                        end_col_offset=39,
                        func=Attribute(
                            lineno=11,
                            col_offset=13,
                            end_lineno=11,
                            end_col_offset=24,
                            value=Name(lineno=11, col_offset=13, end_lineno=11, end_col_offset=19, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=25,
                                end_lineno=11,
                                end_col_offset=38,
                                arg='name',
                                value=Constant(lineno=11, col_offset=30, end_lineno=11, end_col_offset=38, value='Reason', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=13,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=93,
                    name='action_unblacklist_apply',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=13, col_offset=33, end_lineno=13, end_col_offset=37, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            lineno=14,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=93,
                            value=Call(
                                lineno=14,
                                col_offset=15,
                                end_lineno=14,
                                end_col_offset=93,
                                func=Attribute(
                                    lineno=14,
                                    col_offset=15,
                                    end_lineno=14,
                                    end_col_offset=68,
                                    value=Subscript(
                                        lineno=14,
                                        col_offset=15,
                                        end_lineno=14,
                                        end_col_offset=42,
                                        value=Attribute(
                                            lineno=14,
                                            col_offset=15,
                                            end_lineno=14,
                                            end_col_offset=23,
                                            value=Name(lineno=14, col_offset=15, end_lineno=14, end_col_offset=19, id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(lineno=14, col_offset=24, end_lineno=14, end_col_offset=41, value='phone.blacklist', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='action_remove_with_reason',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        lineno=14,
                                        col_offset=69,
                                        end_lineno=14,
                                        end_col_offset=79,
                                        value=Name(lineno=14, col_offset=69, end_lineno=14, end_col_offset=73, id='self', ctx=Load()),
                                        attr='phone',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        lineno=14,
                                        col_offset=81,
                                        end_lineno=14,
                                        end_col_offset=92,
                                        value=Name(lineno=14, col_offset=81, end_lineno=14, end_col_offset=85, id='self', ctx=Load()),
                                        attr='reason',
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