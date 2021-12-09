Module(
    body=[
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ClassDef(
            name='test_res_lang',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_00_intersperse',
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
                        ImportFrom(
                            module='odoo.addons.base.models.res_lang',
                            names=[alias(name='intersperse', asname=None)],
                            level=0,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='', kind=None),
                                        List(elts=[], ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='0', kind=None),
                                        List(elts=[], ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='0', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='012', kind=None),
                                        List(elts=[], ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='012', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='1', kind=None),
                                        List(elts=[], ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='1', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='12', kind=None),
                                        List(elts=[], ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='12', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='123', kind=None),
                                        List(elts=[], ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='123', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='1234', kind=None),
                                        List(elts=[], ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='1234', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='123456789', kind=None),
                                        List(elts=[], ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='123456789', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='&ab%#@1', kind=None),
                                        List(elts=[], ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='&ab%#@1', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='0', kind=None),
                                        List(elts=[], ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='0', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='0', kind=None),
                                        List(
                                            elts=[Constant(value=1, kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='0', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='0', kind=None),
                                        List(
                                            elts=[Constant(value=2, kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='0', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='0', kind=None),
                                        List(
                                            elts=[Constant(value=200, kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='0', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='12345678', kind=None),
                                        List(
                                            elts=[Constant(value=1, kind=None)],
                                            ctx=Load(),
                                        ),
                                        Constant(value='.', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='1234567.8', kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='12345678', kind=None),
                                        List(
                                            elts=[Constant(value=1, kind=None)],
                                            ctx=Load(),
                                        ),
                                        Constant(value='.', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='1234567.8', kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='12345678', kind=None),
                                        List(
                                            elts=[Constant(value=2, kind=None)],
                                            ctx=Load(),
                                        ),
                                        Constant(value='.', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='123456.78', kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='12345678', kind=None),
                                        List(
                                            elts=[
                                                Constant(value=2, kind=None),
                                                Constant(value=1, kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Constant(value='.', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='12345.6.78', kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='12345678', kind=None),
                                        List(
                                            elts=[
                                                Constant(value=2, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Constant(value='.', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='12.34.56.78', kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='12345678', kind=None),
                                        List(
                                            elts=[
                                                UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=1, kind=None),
                                                ),
                                                Constant(value=2, kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Constant(value='.', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='12345678', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='12345678', kind=None),
                                        List(
                                            elts=[
                                                Constant(value=2, kind=None),
                                                UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=1, kind=None),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Constant(value='.', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='123456.78', kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='12345678', kind=None),
                                        List(
                                            elts=[
                                                Constant(value=2, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=1, kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Constant(value='.', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='12.34.56.78', kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='12345678', kind=None),
                                        List(
                                            elts=[
                                                Constant(value=2, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Constant(value='.', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='12.34.56.78', kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='12345678', kind=None),
                                        List(
                                            elts=[
                                                Constant(value=2, kind=None),
                                                Constant(value=0, kind=None),
                                                UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=1, kind=None),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Constant(value='.', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='12.34.56.78', kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='12345678', kind=None),
                                        List(
                                            elts=[
                                                Constant(value=3, kind=None),
                                                Constant(value=3, kind=None),
                                                Constant(value=3, kind=None),
                                                Constant(value=3, kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Constant(value='.', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='12.345.678', kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='abc1234567xy', kind=None),
                                        List(
                                            elts=[Constant(value=2, kind=None)],
                                            ctx=Load(),
                                        ),
                                        Constant(value='.', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='abc1234567.xy', kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='abc1234567xy8', kind=None),
                                        List(
                                            elts=[Constant(value=2, kind=None)],
                                            ctx=Load(),
                                        ),
                                        Constant(value='.', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='abc1234567x.y8', kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='abc12', kind=None),
                                        List(
                                            elts=[Constant(value=3, kind=None)],
                                            ctx=Load(),
                                        ),
                                        Constant(value='.', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='abc12', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='abc12', kind=None),
                                        List(
                                            elts=[Constant(value=2, kind=None)],
                                            ctx=Load(),
                                        ),
                                        Constant(value='.', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='abc12', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Call(
                                    func=Name(id='intersperse', ctx=Load()),
                                    args=[
                                        Constant(value='abc12', kind=None),
                                        List(
                                            elts=[Constant(value=1, kind=None)],
                                            ctx=Load(),
                                        ),
                                        Constant(value='.', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='abc1.2', kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
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
