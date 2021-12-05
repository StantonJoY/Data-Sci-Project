Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=26,
            module='random',
            names=[alias(name='randint', asname=None)],
            level=0,
        ),
        ImportFrom(
            lineno=6,
            col_offset=0,
            end_lineno=6,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=9,
            col_offset=0,
            end_lineno=27,
            end_col_offset=5,
            name='TrackTag',
            bases=[
                Attribute(
                    lineno=9,
                    col_offset=15,
                    end_lineno=9,
                    end_col_offset=27,
                    value=Name(lineno=9, col_offset=15, end_lineno=9, end_col_offset=21, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=29,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=10, col_offset=12, end_lineno=10, end_col_offset=29, value='event.track.tag', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=11,
                    col_offset=4,
                    end_lineno=11,
                    end_col_offset=36,
                    targets=[Name(lineno=11, col_offset=4, end_lineno=11, end_col_offset=16, id='_description', ctx=Store())],
                    value=Constant(lineno=11, col_offset=19, end_lineno=11, end_col_offset=36, value='Event Track Tag', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=42,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=10, id='_order', ctx=Store())],
                    value=Constant(lineno=12, col_offset=13, end_lineno=12, end_col_offset=42, value='category_id, sequence, name', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=14,
                    col_offset=4,
                    end_lineno=15,
                    end_col_offset=29,
                    name='_default_color',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=14, col_offset=23, end_lineno=14, end_col_offset=27, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=29,
                            value=Call(
                                lineno=15,
                                col_offset=15,
                                end_lineno=15,
                                end_col_offset=29,
                                func=Name(lineno=15, col_offset=15, end_lineno=15, end_col_offset=22, id='randint', ctx=Load()),
                                args=[
                                    Constant(lineno=15, col_offset=23, end_lineno=15, end_col_offset=24, value=1, kind=None),
                                    Constant(lineno=15, col_offset=26, end_lineno=15, end_col_offset=28, value=11, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    lineno=17,
                    col_offset=4,
                    end_lineno=17,
                    end_col_offset=49,
                    targets=[Name(lineno=17, col_offset=4, end_lineno=17, end_col_offset=8, id='name', ctx=Store())],
                    value=Call(
                        lineno=17,
                        col_offset=11,
                        end_lineno=17,
                        end_col_offset=49,
                        func=Attribute(
                            lineno=17,
                            col_offset=11,
                            end_lineno=17,
                            end_col_offset=22,
                            value=Name(lineno=17, col_offset=11, end_lineno=17, end_col_offset=17, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=17, col_offset=23, end_lineno=17, end_col_offset=33, value='Tag Name', kind=None)],
                        keywords=[
                            keyword(
                                lineno=17,
                                col_offset=35,
                                end_lineno=17,
                                end_col_offset=48,
                                arg='required',
                                value=Constant(lineno=17, col_offset=44, end_lineno=17, end_col_offset=48, value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=18,
                    col_offset=4,
                    end_lineno=18,
                    end_col_offset=64,
                    targets=[Name(lineno=18, col_offset=4, end_lineno=18, end_col_offset=13, id='track_ids', ctx=Store())],
                    value=Call(
                        lineno=18,
                        col_offset=16,
                        end_lineno=18,
                        end_col_offset=64,
                        func=Attribute(
                            lineno=18,
                            col_offset=16,
                            end_lineno=18,
                            end_col_offset=32,
                            value=Name(lineno=18, col_offset=16, end_lineno=18, end_col_offset=22, id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=18, col_offset=33, end_lineno=18, end_col_offset=46, value='event.track', kind=None)],
                        keywords=[
                            keyword(
                                lineno=18,
                                col_offset=48,
                                end_lineno=18,
                                end_col_offset=63,
                                arg='string',
                                value=Constant(lineno=18, col_offset=55, end_lineno=18, end_col_offset=63, value='Tracks', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=19,
                    col_offset=4,
                    end_lineno=21,
                    end_col_offset=75,
                    targets=[Name(lineno=19, col_offset=4, end_lineno=19, end_col_offset=9, id='color', ctx=Store())],
                    value=Call(
                        lineno=19,
                        col_offset=12,
                        end_lineno=21,
                        end_col_offset=75,
                        func=Attribute(
                            lineno=19,
                            col_offset=12,
                            end_lineno=19,
                            end_col_offset=26,
                            value=Name(lineno=19, col_offset=12, end_lineno=19, end_col_offset=18, id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                lineno=20,
                                col_offset=8,
                                end_lineno=20,
                                end_col_offset=28,
                                arg='string',
                                value=Constant(lineno=20, col_offset=15, end_lineno=20, end_col_offset=28, value='Color Index', kind=None),
                            ),
                            keyword(
                                lineno=20,
                                col_offset=30,
                                end_lineno=20,
                                end_col_offset=72,
                                arg='default',
                                value=Lambda(
                                    lineno=20,
                                    col_offset=38,
                                    end_lineno=20,
                                    end_col_offset=72,
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(lineno=20, col_offset=45, end_lineno=20, end_col_offset=49, arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Call(
                                        lineno=20,
                                        col_offset=51,
                                        end_lineno=20,
                                        end_col_offset=72,
                                        func=Attribute(
                                            lineno=20,
                                            col_offset=51,
                                            end_lineno=20,
                                            end_col_offset=70,
                                            value=Name(lineno=20, col_offset=51, end_lineno=20, end_col_offset=55, id='self', ctx=Load()),
                                            attr='_default_color',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ),
                            keyword(
                                lineno=21,
                                col_offset=8,
                                end_lineno=21,
                                end_col_offset=74,
                                arg='help',
                                value=Constant(lineno=21, col_offset=13, end_lineno=21, end_col_offset=74, value="Note that colorless tags won't be available on the website.", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=22,
                    col_offset=4,
                    end_lineno=22,
                    end_col_offset=53,
                    targets=[Name(lineno=22, col_offset=4, end_lineno=22, end_col_offset=12, id='sequence', ctx=Store())],
                    value=Call(
                        lineno=22,
                        col_offset=15,
                        end_lineno=22,
                        end_col_offset=53,
                        func=Attribute(
                            lineno=22,
                            col_offset=15,
                            end_lineno=22,
                            end_col_offset=29,
                            value=Name(lineno=22, col_offset=15, end_lineno=22, end_col_offset=21, id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=22, col_offset=30, end_lineno=22, end_col_offset=40, value='Sequence', kind=None)],
                        keywords=[
                            keyword(
                                lineno=22,
                                col_offset=42,
                                end_lineno=22,
                                end_col_offset=52,
                                arg='default',
                                value=Constant(lineno=22, col_offset=50, end_lineno=22, end_col_offset=52, value=10, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=23,
                    col_offset=4,
                    end_lineno=23,
                    end_col_offset=101,
                    targets=[Name(lineno=23, col_offset=4, end_lineno=23, end_col_offset=15, id='category_id', ctx=Store())],
                    value=Call(
                        lineno=23,
                        col_offset=18,
                        end_lineno=23,
                        end_col_offset=101,
                        func=Attribute(
                            lineno=23,
                            col_offset=18,
                            end_lineno=23,
                            end_col_offset=33,
                            value=Name(lineno=23, col_offset=18, end_lineno=23, end_col_offset=24, id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=23, col_offset=34, end_lineno=23, end_col_offset=60, value='event.track.tag.category', kind=None)],
                        keywords=[
                            keyword(
                                lineno=23,
                                col_offset=62,
                                end_lineno=23,
                                end_col_offset=79,
                                arg='string',
                                value=Constant(lineno=23, col_offset=69, end_lineno=23, end_col_offset=79, value='Category', kind=None),
                            ),
                            keyword(
                                lineno=23,
                                col_offset=81,
                                end_lineno=23,
                                end_col_offset=100,
                                arg='ondelete',
                                value=Constant(lineno=23, col_offset=90, end_lineno=23, end_col_offset=100, value='set null', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=25,
                    col_offset=4,
                    end_lineno=27,
                    end_col_offset=5,
                    targets=[Name(lineno=25, col_offset=4, end_lineno=25, end_col_offset=20, id='_sql_constraints', ctx=Store())],
                    value=List(
                        lineno=25,
                        col_offset=23,
                        end_lineno=27,
                        end_col_offset=5,
                        elts=[
                            Tuple(
                                lineno=26,
                                col_offset=8,
                                end_lineno=26,
                                end_col_offset=67,
                                elts=[
                                    Constant(lineno=26, col_offset=9, end_lineno=26, end_col_offset=20, value='name_uniq', kind=None),
                                    Constant(lineno=26, col_offset=22, end_lineno=26, end_col_offset=37, value='unique (name)', kind=None),
                                    Constant(lineno=26, col_offset=39, end_lineno=26, end_col_offset=66, value='Tag name already exists !', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)