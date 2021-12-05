Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=29,
            module='odoo.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        ClassDef(
            lineno=6,
            col_offset=0,
            end_lineno=22,
            end_col_offset=55,
            name='TestGBF',
            bases=[
                Attribute(
                    lineno=6,
                    col_offset=14,
                    end_lineno=6,
                    end_col_offset=36,
                    value=Name(lineno=6, col_offset=14, end_lineno=6, end_col_offset=20, id='common', ctx=Load()),
                    attr='TransactionCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    lineno=7,
                    col_offset=4,
                    end_lineno=22,
                    end_col_offset=55,
                    name='test_group_by_full',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=7, col_offset=27, end_lineno=7, end_col_offset=31, arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=8,
                            col_offset=8,
                            end_lineno=8,
                            end_col_offset=55,
                            targets=[Name(lineno=8, col_offset=8, end_lineno=8, end_col_offset=11, id='Sub', ctx=Store())],
                            value=Subscript(
                                lineno=8,
                                col_offset=14,
                                end_lineno=8,
                                end_col_offset=55,
                                value=Attribute(
                                    lineno=8,
                                    col_offset=14,
                                    end_lineno=8,
                                    end_col_offset=22,
                                    value=Name(lineno=8, col_offset=14, end_lineno=8, end_col_offset=18, id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(lineno=8, col_offset=23, end_lineno=8, end_col_offset=54, value='test_converter.test_model.sub', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            lineno=9,
                            col_offset=8,
                            end_lineno=9,
                            end_col_offset=50,
                            targets=[Name(lineno=9, col_offset=8, end_lineno=9, end_col_offset=10, id='TM', ctx=Store())],
                            value=Subscript(
                                lineno=9,
                                col_offset=13,
                                end_lineno=9,
                                end_col_offset=50,
                                value=Attribute(
                                    lineno=9,
                                    col_offset=13,
                                    end_lineno=9,
                                    end_col_offset=21,
                                    value=Name(lineno=9, col_offset=13, end_lineno=9, end_col_offset=17, id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(lineno=9, col_offset=22, end_lineno=9, end_col_offset=49, value='test_converter.test_model', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=12,
                            col_offset=8,
                            end_lineno=12,
                            end_col_offset=31,
                            value=Call(
                                lineno=12,
                                col_offset=8,
                                end_lineno=12,
                                end_col_offset=31,
                                func=Attribute(
                                    lineno=12,
                                    col_offset=8,
                                    end_lineno=12,
                                    end_col_offset=29,
                                    value=Call(
                                        lineno=12,
                                        col_offset=8,
                                        end_lineno=12,
                                        end_col_offset=22,
                                        func=Attribute(
                                            lineno=12,
                                            col_offset=8,
                                            end_lineno=12,
                                            end_col_offset=18,
                                            value=Name(lineno=12, col_offset=8, end_lineno=12, end_col_offset=11, id='Sub', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(lineno=12, col_offset=19, end_lineno=12, end_col_offset=21, elts=[], ctx=Load())],
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
                            lineno=14,
                            col_offset=8,
                            end_lineno=14,
                            end_col_offset=75,
                            targets=[Name(lineno=14, col_offset=8, end_lineno=14, end_col_offset=16, id='subs_ids', ctx=Store())],
                            value=ListComp(
                                lineno=14,
                                col_offset=19,
                                end_lineno=14,
                                end_col_offset=75,
                                elt=Attribute(
                                    lineno=14,
                                    col_offset=20,
                                    end_lineno=14,
                                    end_col_offset=56,
                                    value=Call(
                                        lineno=14,
                                        col_offset=20,
                                        end_lineno=14,
                                        end_col_offset=53,
                                        func=Attribute(
                                            lineno=14,
                                            col_offset=20,
                                            end_lineno=14,
                                            end_col_offset=30,
                                            value=Name(lineno=14, col_offset=20, end_lineno=14, end_col_offset=23, id='Sub', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                lineno=14,
                                                col_offset=31,
                                                end_lineno=14,
                                                end_col_offset=52,
                                                keys=[Constant(lineno=14, col_offset=32, end_lineno=14, end_col_offset=38, value='name', kind=None)],
                                                values=[
                                                    BinOp(
                                                        lineno=14,
                                                        col_offset=40,
                                                        end_lineno=14,
                                                        end_col_offset=51,
                                                        left=Constant(lineno=14, col_offset=40, end_lineno=14, end_col_offset=47, value='sub%d', kind=None),
                                                        op=Mod(),
                                                        right=Name(lineno=14, col_offset=50, end_lineno=14, end_col_offset=51, id='i', ctx=Load()),
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
                                        target=Name(lineno=14, col_offset=61, end_lineno=14, end_col_offset=62, id='i', ctx=Store()),
                                        iter=Call(
                                            lineno=14,
                                            col_offset=66,
                                            end_lineno=14,
                                            end_col_offset=74,
                                            func=Name(lineno=14, col_offset=66, end_lineno=14, end_col_offset=71, id='range', ctx=Load()),
                                            args=[Constant(lineno=14, col_offset=72, end_lineno=14, end_col_offset=73, value=5, kind=None)],
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
                            lineno=15,
                            col_offset=8,
                            end_lineno=15,
                            end_col_offset=76,
                            targets=[Name(lineno=15, col_offset=8, end_lineno=15, end_col_offset=14, id='tm_ids', ctx=Store())],
                            value=ListComp(
                                lineno=15,
                                col_offset=17,
                                end_lineno=15,
                                end_col_offset=76,
                                elt=Attribute(
                                    lineno=15,
                                    col_offset=18,
                                    end_lineno=15,
                                    end_col_offset=57,
                                    value=Call(
                                        lineno=15,
                                        col_offset=18,
                                        end_lineno=15,
                                        end_col_offset=54,
                                        func=Attribute(
                                            lineno=15,
                                            col_offset=18,
                                            end_lineno=15,
                                            end_col_offset=27,
                                            value=Name(lineno=15, col_offset=18, end_lineno=15, end_col_offset=20, id='TM', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                lineno=15,
                                                col_offset=28,
                                                end_lineno=15,
                                                end_col_offset=53,
                                                keys=[Constant(lineno=15, col_offset=29, end_lineno=15, end_col_offset=39, value='many2one', kind=None)],
                                                values=[
                                                    Subscript(
                                                        lineno=15,
                                                        col_offset=41,
                                                        end_lineno=15,
                                                        end_col_offset=52,
                                                        value=Name(lineno=15, col_offset=41, end_lineno=15, end_col_offset=49, id='subs_ids', ctx=Load()),
                                                        slice=Name(lineno=15, col_offset=50, end_lineno=15, end_col_offset=51, id='i', ctx=Load()),
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
                                        target=Name(lineno=15, col_offset=62, end_lineno=15, end_col_offset=63, id='i', ctx=Store()),
                                        iter=Call(
                                            lineno=15,
                                            col_offset=67,
                                            end_lineno=15,
                                            end_col_offset=75,
                                            func=Name(lineno=15, col_offset=67, end_lineno=15, end_col_offset=72, id='range', ctx=Load()),
                                            args=[Constant(lineno=15, col_offset=73, end_lineno=15, end_col_offset=74, value=3, kind=None)],
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
                            lineno=17,
                            col_offset=8,
                            end_lineno=17,
                            end_col_offset=46,
                            targets=[Name(lineno=17, col_offset=8, end_lineno=17, end_col_offset=14, id='domain', ctx=Store())],
                            value=List(
                                lineno=17,
                                col_offset=17,
                                end_lineno=17,
                                end_col_offset=46,
                                elts=[
                                    Tuple(
                                        lineno=17,
                                        col_offset=18,
                                        end_lineno=17,
                                        end_col_offset=45,
                                        elts=[
                                            Constant(lineno=17, col_offset=19, end_lineno=17, end_col_offset=23, value='id', kind=None),
                                            Constant(lineno=17, col_offset=25, end_lineno=17, end_col_offset=29, value='in', kind=None),
                                            Call(
                                                lineno=17,
                                                col_offset=31,
                                                end_lineno=17,
                                                end_col_offset=44,
                                                func=Name(lineno=17, col_offset=31, end_lineno=17, end_col_offset=36, id='tuple', ctx=Load()),
                                                args=[Name(lineno=17, col_offset=37, end_lineno=17, end_col_offset=43, id='tm_ids', ctx=Load())],
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
                            lineno=18,
                            col_offset=8,
                            end_lineno=18,
                            end_col_offset=77,
                            targets=[Name(lineno=18, col_offset=8, end_lineno=18, end_col_offset=10, id='rg', ctx=Store())],
                            value=Call(
                                lineno=18,
                                col_offset=13,
                                end_lineno=18,
                                end_col_offset=77,
                                func=Attribute(
                                    lineno=18,
                                    col_offset=13,
                                    end_lineno=18,
                                    end_col_offset=26,
                                    value=Name(lineno=18, col_offset=13, end_lineno=18, end_col_offset=15, id='TM', ctx=Load()),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=18, col_offset=27, end_lineno=18, end_col_offset=33, id='domain', ctx=Load())],
                                keywords=[
                                    keyword(
                                        lineno=18,
                                        col_offset=35,
                                        end_lineno=18,
                                        end_col_offset=54,
                                        arg='fields',
                                        value=List(
                                            lineno=18,
                                            col_offset=42,
                                            end_lineno=18,
                                            end_col_offset=54,
                                            elts=[Constant(lineno=18, col_offset=43, end_lineno=18, end_col_offset=53, value='many2one', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        lineno=18,
                                        col_offset=56,
                                        end_lineno=18,
                                        end_col_offset=76,
                                        arg='groupby',
                                        value=List(
                                            lineno=18,
                                            col_offset=64,
                                            end_lineno=18,
                                            end_col_offset=76,
                                            elts=[Constant(lineno=18, col_offset=65, end_lineno=18, end_col_offset=75, value='many2one', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            lineno=20,
                            col_offset=8,
                            end_lineno=20,
                            end_col_offset=48,
                            value=Call(
                                lineno=20,
                                col_offset=8,
                                end_lineno=20,
                                end_col_offset=48,
                                func=Attribute(
                                    lineno=20,
                                    col_offset=8,
                                    end_lineno=20,
                                    end_col_offset=24,
                                    value=Name(lineno=20, col_offset=8, end_lineno=20, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        lineno=20,
                                        col_offset=25,
                                        end_lineno=20,
                                        end_col_offset=32,
                                        func=Name(lineno=20, col_offset=25, end_lineno=20, end_col_offset=28, id='len', ctx=Load()),
                                        args=[Name(lineno=20, col_offset=29, end_lineno=20, end_col_offset=31, id='rg', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        lineno=20,
                                        col_offset=34,
                                        end_lineno=20,
                                        end_col_offset=47,
                                        func=Name(lineno=20, col_offset=34, end_lineno=20, end_col_offset=37, id='len', ctx=Load()),
                                        args=[Name(lineno=20, col_offset=38, end_lineno=20, end_col_offset=46, id='subs_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=21,
                            col_offset=8,
                            end_lineno=21,
                            end_col_offset=54,
                            targets=[Name(lineno=21, col_offset=8, end_lineno=21, end_col_offset=15, id='rg_subs', ctx=Store())],
                            value=Call(
                                lineno=21,
                                col_offset=18,
                                end_lineno=21,
                                end_col_offset=54,
                                func=Name(lineno=21, col_offset=18, end_lineno=21, end_col_offset=24, id='sorted', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        lineno=21,
                                        col_offset=24,
                                        end_lineno=21,
                                        end_col_offset=54,
                                        elt=Subscript(
                                            lineno=21,
                                            col_offset=25,
                                            end_lineno=21,
                                            end_col_offset=41,
                                            value=Subscript(
                                                lineno=21,
                                                col_offset=25,
                                                end_lineno=21,
                                                end_col_offset=38,
                                                value=Name(lineno=21, col_offset=25, end_lineno=21, end_col_offset=26, id='g', ctx=Load()),
                                                slice=Constant(lineno=21, col_offset=27, end_lineno=21, end_col_offset=37, value='many2one', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(lineno=21, col_offset=39, end_lineno=21, end_col_offset=40, value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(lineno=21, col_offset=46, end_lineno=21, end_col_offset=47, id='g', ctx=Store()),
                                                iter=Name(lineno=21, col_offset=51, end_lineno=21, end_col_offset=53, id='rg', ctx=Load()),
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
                            lineno=22,
                            col_offset=8,
                            end_lineno=22,
                            end_col_offset=55,
                            value=Call(
                                lineno=22,
                                col_offset=8,
                                end_lineno=22,
                                end_col_offset=55,
                                func=Attribute(
                                    lineno=22,
                                    col_offset=8,
                                    end_lineno=22,
                                    end_col_offset=28,
                                    value=Name(lineno=22, col_offset=8, end_lineno=22, end_col_offset=12, id='self', ctx=Load()),
                                    attr='assertListEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(lineno=22, col_offset=29, end_lineno=22, end_col_offset=36, id='rg_subs', ctx=Load()),
                                    Call(
                                        lineno=22,
                                        col_offset=38,
                                        end_lineno=22,
                                        end_col_offset=54,
                                        func=Name(lineno=22, col_offset=38, end_lineno=22, end_col_offset=44, id='sorted', ctx=Load()),
                                        args=[Name(lineno=22, col_offset=45, end_lineno=22, end_col_offset=53, id='subs_ids', ctx=Load())],
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