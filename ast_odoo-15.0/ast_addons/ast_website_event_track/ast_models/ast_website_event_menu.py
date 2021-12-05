Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=12,
            end_col_offset=67,
            name='EventMenu',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=16,
                    end_lineno=7,
                    end_col_offset=28,
                    value=Name(lineno=7, col_offset=16, end_lineno=7, end_col_offset=22, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=8,
                    col_offset=4,
                    end_lineno=8,
                    end_col_offset=35,
                    targets=[Name(lineno=8, col_offset=4, end_lineno=8, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=Constant(lineno=8, col_offset=15, end_lineno=8, end_col_offset=35, value='website.event.menu', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=67,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=13, id='menu_type', ctx=Store())],
                    value=Call(
                        lineno=10,
                        col_offset=16,
                        end_lineno=12,
                        end_col_offset=67,
                        func=Attribute(
                            lineno=10,
                            col_offset=16,
                            end_lineno=10,
                            end_col_offset=32,
                            value=Name(lineno=10, col_offset=16, end_lineno=10, end_col_offset=22, id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=11,
                                col_offset=8,
                                end_lineno=11,
                                end_col_offset=100,
                                arg='selection_add',
                                value=List(
                                    lineno=11,
                                    col_offset=22,
                                    end_lineno=11,
                                    end_col_offset=100,
                                    elts=[
                                        Tuple(
                                            lineno=11,
                                            col_offset=23,
                                            end_lineno=11,
                                            end_col_offset=54,
                                            elts=[
                                                Constant(lineno=11, col_offset=24, end_lineno=11, end_col_offset=31, value='track', kind=None),
                                                Constant(lineno=11, col_offset=33, end_lineno=11, end_col_offset=53, value='Event Tracks Menus', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            lineno=11,
                                            col_offset=56,
                                            end_lineno=11,
                                            end_col_offset=99,
                                            elts=[
                                                Constant(lineno=11, col_offset=57, end_lineno=11, end_col_offset=73, value='track_proposal', kind=None),
                                                Constant(lineno=11, col_offset=75, end_lineno=11, end_col_offset=98, value='Event Proposals Menus', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                lineno=12,
                                col_offset=8,
                                end_lineno=12,
                                end_col_offset=66,
                                arg='ondelete',
                                value=Dict(
                                    lineno=12,
                                    col_offset=17,
                                    end_lineno=12,
                                    end_col_offset=66,
                                    keys=[
                                        Constant(lineno=12, col_offset=18, end_lineno=12, end_col_offset=25, value='track', kind=None),
                                        Constant(lineno=12, col_offset=38, end_lineno=12, end_col_offset=54, value='track_proposal', kind=None),
                                    ],
                                    values=[
                                        Constant(lineno=12, col_offset=27, end_lineno=12, end_col_offset=36, value='cascade', kind=None),
                                        Constant(lineno=12, col_offset=56, end_lineno=12, end_col_offset=65, value='cascade', kind=None),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)