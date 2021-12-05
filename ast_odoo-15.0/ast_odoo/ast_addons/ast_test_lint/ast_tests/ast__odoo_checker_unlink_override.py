Module(
    body=[
        Import(
            lineno=1,
            col_offset=0,
            end_lineno=1,
            end_col_offset=14,
            names=[alias(name='astroid', asname=None)],
        ),
        ImportFrom(
            lineno=2,
            col_offset=0,
            end_lineno=2,
            end_col_offset=39,
            module='pylint',
            names=[
                alias(name='checkers', asname=None),
                alias(name='interfaces', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=5,
            col_offset=0,
            end_lineno=33,
            end_col_offset=34,
            name='OdooBaseChecker',
            bases=[
                Attribute(
                    lineno=5,
                    col_offset=22,
                    end_lineno=5,
                    end_col_offset=42,
                    value=Name(lineno=5, col_offset=22, end_lineno=5, end_col_offset=30, id='checkers', ctx=Load()),
                    attr='BaseChecker',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=6,
                    col_offset=4,
                    end_lineno=6,
                    end_col_offset=47,
                    targets=[Name(lineno=6, col_offset=4, end_lineno=6, end_col_offset=18, id='__implements__', ctx=Store())],
                    value=Attribute(
                        lineno=6,
                        col_offset=21,
                        end_lineno=6,
                        end_col_offset=47,
                        value=Name(lineno=6, col_offset=21, end_lineno=6, end_col_offset=31, id='interfaces', ctx=Load()),
                        attr='IAstroidChecker',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=7,
                    col_offset=4,
                    end_lineno=7,
                    end_col_offset=17,
                    targets=[Name(lineno=7, col_offset=4, end_lineno=7, end_col_offset=8, id='name', ctx=Store())],
                    value=Constant(lineno=7, col_offset=11, end_lineno=7, end_col_offset=17, value='odoo', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=18,
                    end_col_offset=5,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=8, id='msgs', ctx=Store())],
                    value=Dict(
                        lineno=9,
                        col_offset=11,
                        end_lineno=18,
                        end_col_offset=5,
                        keys=[Constant(lineno=10, col_offset=8, end_lineno=10, end_col_offset=15, value='E8503', kind=None)],
                        values=[
                            Tuple(
                                lineno=10,
                                col_offset=17,
                                end_lineno=17,
                                end_col_offset=9,
                                elts=[
                                    Constant(lineno=11, col_offset=12, end_lineno=11, end_col_offset=43, value='Raise inside unlink override.', kind=None),
                                    Constant(lineno=12, col_offset=12, end_lineno=12, end_col_offset=35, value='raise-unlink-override', kind=None),
                                    Constant(lineno=13, col_offset=12, end_lineno=16, end_col_offset=63, value='Raising errors is not allowed inside unlink overrides, you can create a method and decorate it with @api.ondelete(at_uninstall=False), only use at_uninstall=True if you know what you are doing.', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=21,
                    col_offset=4,
                    end_lineno=22,
                    end_col_offset=86,
                    name='_inherits_BaseModel',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(lineno=21, col_offset=28, end_lineno=21, end_col_offset=32, arg='node', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            lineno=22,
                            col_offset=8,
                            end_lineno=22,
                            end_col_offset=86,
                            value=Call(
                                lineno=22,
                                col_offset=15,
                                end_lineno=22,
                                end_col_offset=86,
                                func=Name(lineno=22, col_offset=15, end_lineno=22, end_col_offset=18, id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        lineno=22,
                                        col_offset=18,
                                        end_lineno=22,
                                        end_col_offset=86,
                                        elt=Compare(
                                            lineno=22,
                                            col_offset=19,
                                            end_lineno=22,
                                            end_col_offset=59,
                                            left=Call(
                                                lineno=22,
                                                col_offset=19,
                                                end_lineno=22,
                                                end_col_offset=44,
                                                func=Name(lineno=22, col_offset=19, end_lineno=22, end_col_offset=26, id='getattr', ctx=Load()),
                                                args=[
                                                    Name(lineno=22, col_offset=27, end_lineno=22, end_col_offset=28, id='n', ctx=Load()),
                                                    Constant(lineno=22, col_offset=30, end_lineno=22, end_col_offset=36, value='name', kind=None),
                                                    Constant(lineno=22, col_offset=38, end_lineno=22, end_col_offset=43, value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(lineno=22, col_offset=48, end_lineno=22, end_col_offset=59, value='BaseModel', kind=None)],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(lineno=22, col_offset=64, end_lineno=22, end_col_offset=65, id='n', ctx=Store()),
                                                iter=Call(
                                                    lineno=22,
                                                    col_offset=69,
                                                    end_lineno=22,
                                                    end_col_offset=85,
                                                    func=Attribute(
                                                        lineno=22,
                                                        col_offset=69,
                                                        end_lineno=22,
                                                        end_col_offset=83,
                                                        value=Name(lineno=22, col_offset=69, end_lineno=22, end_col_offset=73, id='node', ctx=Load()),
                                                        attr='ancestors',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(lineno=20, col_offset=5, end_lineno=20, end_col_offset=17, id='staticmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    lineno=24,
                    col_offset=4,
                    end_lineno=33,
                    end_col_offset=34,
                    name='visit_raise',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(lineno=24, col_offset=20, end_lineno=24, end_col_offset=24, arg='self', annotation=None, type_comment=None),
                            arg(lineno=24, col_offset=26, end_lineno=24, end_col_offset=30, arg='node', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            lineno=25,
                            col_offset=8,
                            end_lineno=25,
                            end_col_offset=28,
                            targets=[Name(lineno=25, col_offset=8, end_lineno=25, end_col_offset=14, id='parent', ctx=Store())],
                            value=Attribute(
                                lineno=25,
                                col_offset=17,
                                end_lineno=25,
                                end_col_offset=28,
                                value=Name(lineno=25, col_offset=17, end_lineno=25, end_col_offset=21, id='node', ctx=Load()),
                                attr='parent',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        While(
                            lineno=26,
                            col_offset=8,
                            end_lineno=33,
                            end_col_offset=34,
                            test=Name(lineno=26, col_offset=14, end_lineno=26, end_col_offset=20, id='parent', ctx=Load()),
                            body=[
                                If(
                                    lineno=27,
                                    col_offset=12,
                                    end_lineno=32,
                                    end_col_offset=24,
                                    test=BoolOp(
                                        lineno=27,
                                        col_offset=15,
                                        end_lineno=27,
                                        end_col_offset=82,
                                        op=And(),
                                        values=[
                                            Call(
                                                lineno=27,
                                                col_offset=15,
                                                end_lineno=27,
                                                end_col_offset=54,
                                                func=Name(lineno=27, col_offset=15, end_lineno=27, end_col_offset=25, id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(lineno=27, col_offset=26, end_lineno=27, end_col_offset=32, id='parent', ctx=Load()),
                                                    Attribute(
                                                        lineno=27,
                                                        col_offset=34,
                                                        end_lineno=27,
                                                        end_col_offset=53,
                                                        value=Name(lineno=27, col_offset=34, end_lineno=27, end_col_offset=41, id='astroid', ctx=Load()),
                                                        attr='FunctionDef',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Compare(
                                                lineno=27,
                                                col_offset=59,
                                                end_lineno=27,
                                                end_col_offset=82,
                                                left=Attribute(
                                                    lineno=27,
                                                    col_offset=59,
                                                    end_lineno=27,
                                                    end_col_offset=70,
                                                    value=Name(lineno=27, col_offset=59, end_lineno=27, end_col_offset=65, id='parent', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(lineno=27, col_offset=74, end_lineno=27, end_col_offset=82, value='unlink', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            lineno=28,
                                            col_offset=16,
                                            end_lineno=28,
                                            end_col_offset=38,
                                            targets=[Name(lineno=28, col_offset=16, end_lineno=28, end_col_offset=22, id='parent', ctx=Store())],
                                            value=Attribute(
                                                lineno=28,
                                                col_offset=25,
                                                end_lineno=28,
                                                end_col_offset=38,
                                                value=Name(lineno=28, col_offset=25, end_lineno=28, end_col_offset=31, id='parent', ctx=Load()),
                                                attr='parent',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            lineno=29,
                                            col_offset=16,
                                            end_lineno=31,
                                            end_col_offset=25,
                                            test=BoolOp(
                                                lineno=29,
                                                col_offset=19,
                                                end_lineno=29,
                                                end_col_offset=92,
                                                op=And(),
                                                values=[
                                                    Call(
                                                        lineno=29,
                                                        col_offset=19,
                                                        end_lineno=29,
                                                        end_col_offset=55,
                                                        func=Name(lineno=29, col_offset=19, end_lineno=29, end_col_offset=29, id='isinstance', ctx=Load()),
                                                        args=[
                                                            Name(lineno=29, col_offset=30, end_lineno=29, end_col_offset=36, id='parent', ctx=Load()),
                                                            Attribute(
                                                                lineno=29,
                                                                col_offset=38,
                                                                end_lineno=29,
                                                                end_col_offset=54,
                                                                value=Name(lineno=29, col_offset=38, end_lineno=29, end_col_offset=45, id='astroid', ctx=Load()),
                                                                attr='ClassDef',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        lineno=29,
                                                        col_offset=60,
                                                        end_lineno=29,
                                                        end_col_offset=92,
                                                        func=Attribute(
                                                            lineno=29,
                                                            col_offset=60,
                                                            end_lineno=29,
                                                            end_col_offset=84,
                                                            value=Name(lineno=29, col_offset=60, end_lineno=29, end_col_offset=64, id='self', ctx=Load()),
                                                            attr='_inherits_BaseModel',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(lineno=29, col_offset=85, end_lineno=29, end_col_offset=91, id='parent', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    lineno=30,
                                                    col_offset=20,
                                                    end_lineno=30,
                                                    end_col_offset=72,
                                                    value=Call(
                                                        lineno=30,
                                                        col_offset=20,
                                                        end_lineno=30,
                                                        end_col_offset=72,
                                                        func=Attribute(
                                                            lineno=30,
                                                            col_offset=20,
                                                            end_lineno=30,
                                                            end_col_offset=36,
                                                            value=Name(lineno=30, col_offset=20, end_lineno=30, end_col_offset=24, id='self', ctx=Load()),
                                                            attr='add_message',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(lineno=30, col_offset=37, end_lineno=30, end_col_offset=60, value='raise-unlink-override', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                lineno=30,
                                                                col_offset=62,
                                                                end_lineno=30,
                                                                end_col_offset=71,
                                                                arg='node',
                                                                value=Name(lineno=30, col_offset=67, end_lineno=30, end_col_offset=71, id='node', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                Break(lineno=31, col_offset=20, end_lineno=31, end_col_offset=25),
                                            ],
                                            orelse=[],
                                        ),
                                        Continue(lineno=32, col_offset=16, end_lineno=32, end_col_offset=24),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    lineno=33,
                                    col_offset=12,
                                    end_lineno=33,
                                    end_col_offset=34,
                                    targets=[Name(lineno=33, col_offset=12, end_lineno=33, end_col_offset=18, id='parent', ctx=Store())],
                                    value=Attribute(
                                        lineno=33,
                                        col_offset=21,
                                        end_lineno=33,
                                        end_col_offset=34,
                                        value=Name(lineno=33, col_offset=21, end_lineno=33, end_col_offset=27, id='parent', ctx=Load()),
                                        attr='parent',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        FunctionDef(
            lineno=35,
            col_offset=0,
            end_lineno=36,
            end_col_offset=52,
            name='register',
            args=arguments(
                posonlyargs=[],
                args=[arg(lineno=35, col_offset=13, end_lineno=35, end_col_offset=19, arg='linter', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    lineno=36,
                    col_offset=4,
                    end_lineno=36,
                    end_col_offset=52,
                    value=Call(
                        lineno=36,
                        col_offset=4,
                        end_lineno=36,
                        end_col_offset=52,
                        func=Attribute(
                            lineno=36,
                            col_offset=4,
                            end_lineno=36,
                            end_col_offset=27,
                            value=Name(lineno=36, col_offset=4, end_lineno=36, end_col_offset=10, id='linter', ctx=Load()),
                            attr='register_checker',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                lineno=36,
                                col_offset=28,
                                end_lineno=36,
                                end_col_offset=51,
                                func=Name(lineno=36, col_offset=28, end_lineno=36, end_col_offset=43, id='OdooBaseChecker', ctx=Load()),
                                args=[Name(lineno=36, col_offset=44, end_lineno=36, end_col_offset=50, id='linter', ctx=Load())],
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
    type_ignores=[],
)