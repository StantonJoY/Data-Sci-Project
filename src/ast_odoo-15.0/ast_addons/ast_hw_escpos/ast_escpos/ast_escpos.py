Module(
    body=[
        ImportFrom(
            module='__future__',
            names=[alias(name='print_function', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='copy', asname=None)],
        ),
        Import(
            names=[alias(name='io', asname=None)],
        ),
        Import(
            names=[alias(name='math', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='traceback', asname=None)],
        ),
        Import(
            names=[alias(name='codecs', asname=None)],
        ),
        ImportFrom(
            module='hashlib',
            names=[alias(name='md5', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='PIL',
            names=[alias(name='Image', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='xml.etree',
            names=[alias(name='ElementTree', asname='ET')],
            level=0,
        ),
        Try(
            body=[
                Import(
                    names=[alias(name='jcconv', asname=None)],
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        Assign(
                            targets=[Name(id='jcconv', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                ),
            ],
            orelse=[],
            finalbody=[],
        ),
        Try(
            body=[
                Import(
                    names=[alias(name='qrcode', asname=None)],
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        Assign(
                            targets=[Name(id='qrcode', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                ),
            ],
            orelse=[],
            finalbody=[],
        ),
        ImportFrom(
            module='constants',
            names=[alias(name='*', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='exceptions',
            names=[alias(name='*', asname=None)],
            level=1,
        ),
        FunctionDef(
            name='utfstr',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='stuff', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' converts stuff to string and does without failing if stuff is a utf8 string ', kind=None),
                ),
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='stuff', ctx=Load()),
                            Name(id='str', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Return(
                            value=Name(id='stuff', ctx=Load()),
                        ),
                    ],
                    orelse=[
                        Return(
                            value=Call(
                                func=Name(id='str', ctx=Load()),
                                args=[Name(id='stuff', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='StyleStack',
            bases=[],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' \n    The stylestack is used by the xml receipt serializer to compute the active styles along the xml\n    document. Styles are just xml attributes, there is no css mechanism. But the style applied by\n    the attributes are inherited by deeper nodes.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='stack',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='defaults',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='align', kind=None),
                                    Constant(value='underline', kind=None),
                                    Constant(value='bold', kind=None),
                                    Constant(value='size', kind=None),
                                    Constant(value='font', kind=None),
                                    Constant(value='width', kind=None),
                                    Constant(value='indent', kind=None),
                                    Constant(value='tabwidth', kind=None),
                                    Constant(value='bullet', kind=None),
                                    Constant(value='line-ratio', kind=None),
                                    Constant(value='color', kind=None),
                                    Constant(value='value-decimals', kind=None),
                                    Constant(value='value-symbol', kind=None),
                                    Constant(value='value-symbol-position', kind=None),
                                    Constant(value='value-autoint', kind=None),
                                    Constant(value='value-decimals-separator', kind=None),
                                    Constant(value='value-thousands-separator', kind=None),
                                    Constant(value='value-width', kind=None),
                                ],
                                values=[
                                    Constant(value='left', kind=None),
                                    Constant(value='off', kind=None),
                                    Constant(value='off', kind=None),
                                    Constant(value='normal', kind=None),
                                    Constant(value='a', kind=None),
                                    Constant(value=48, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=2, kind=None),
                                    Constant(value=' - ', kind=None),
                                    Constant(value=0.5, kind=None),
                                    Constant(value='black', kind=None),
                                    Constant(value=2, kind=None),
                                    Constant(value='', kind=None),
                                    Constant(value='after', kind=None),
                                    Constant(value='off', kind=None),
                                    Constant(value='.', kind=None),
                                    Constant(value=',', kind=None),
                                    Constant(value=0, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='types',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='width', kind=None),
                                    Constant(value='indent', kind=None),
                                    Constant(value='tabwidth', kind=None),
                                    Constant(value='line-ratio', kind=None),
                                    Constant(value='value-decimals', kind=None),
                                    Constant(value='value-width', kind=None),
                                ],
                                values=[
                                    Constant(value='int', kind=None),
                                    Constant(value='int', kind=None),
                                    Constant(value='int', kind=None),
                                    Constant(value='float', kind=None),
                                    Constant(value='int', kind=None),
                                    Constant(value='int', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='cmds',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='align', kind=None),
                                    Constant(value='underline', kind=None),
                                    Constant(value='bold', kind=None),
                                    Constant(value='font', kind=None),
                                    Constant(value='size', kind=None),
                                    Constant(value='color', kind=None),
                                ],
                                values=[
                                    Dict(
                                        keys=[
                                            Constant(value='left', kind=None),
                                            Constant(value='right', kind=None),
                                            Constant(value='center', kind=None),
                                            Constant(value='_order', kind=None),
                                        ],
                                        values=[
                                            Name(id='TXT_ALIGN_LT', ctx=Load()),
                                            Name(id='TXT_ALIGN_RT', ctx=Load()),
                                            Name(id='TXT_ALIGN_CT', ctx=Load()),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='off', kind=None),
                                            Constant(value='on', kind=None),
                                            Constant(value='double', kind=None),
                                            Constant(value='_order', kind=None),
                                        ],
                                        values=[
                                            Name(id='TXT_UNDERL_OFF', ctx=Load()),
                                            Name(id='TXT_UNDERL_ON', ctx=Load()),
                                            Name(id='TXT_UNDERL2_ON', ctx=Load()),
                                            Constant(value=10, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='off', kind=None),
                                            Constant(value='on', kind=None),
                                            Constant(value='_order', kind=None),
                                        ],
                                        values=[
                                            Name(id='TXT_BOLD_OFF', ctx=Load()),
                                            Name(id='TXT_BOLD_ON', ctx=Load()),
                                            Constant(value=10, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='a', kind=None),
                                            Constant(value='b', kind=None),
                                            Constant(value='_order', kind=None),
                                        ],
                                        values=[
                                            Name(id='TXT_FONT_A', ctx=Load()),
                                            Name(id='TXT_FONT_B', ctx=Load()),
                                            Constant(value=10, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='normal', kind=None),
                                            Constant(value='double-height', kind=None),
                                            Constant(value='double-width', kind=None),
                                            Constant(value='double', kind=None),
                                            Constant(value='_order', kind=None),
                                        ],
                                        values=[
                                            Name(id='TXT_NORMAL', ctx=Load()),
                                            Name(id='TXT_2HEIGHT', ctx=Load()),
                                            Name(id='TXT_2WIDTH', ctx=Load()),
                                            Name(id='TXT_DOUBLE', ctx=Load()),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='black', kind=None),
                                            Constant(value='red', kind=None),
                                            Constant(value='_order', kind=None),
                                        ],
                                        values=[
                                            Name(id='TXT_COLOR_BLACK', ctx=Load()),
                                            Name(id='TXT_COLOR_RED', ctx=Load()),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='push',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='defaults',
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
                FunctionDef(
                    name='get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='style', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" what's the value of a style at the current stack level", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='level', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='stack',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                op=Sub(),
                                right=Constant(value=1, kind=None),
                            ),
                            type_comment=None,
                        ),
                        While(
                            test=Compare(
                                left=Name(id='level', ctx=Load()),
                                ops=[GtE()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='style', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='stack',
                                                    ctx=Load(),
                                                ),
                                                slice=Name(id='level', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='stack',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='level', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                slice=Name(id='style', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='level', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='level', ctx=Load()),
                                                op=Sub(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=None, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='enforce_type',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='attr', annotation=None, type_comment=None),
                            arg(arg='val', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="converts a value to the attribute's type", kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Compare(
                                    left=Name(id='attr', ctx=Load()),
                                    ops=[In()],
                                    comparators=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='types',
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='utfstr', ctx=Load()),
                                        args=[Name(id='val', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='types',
                                                ctx=Load(),
                                            ),
                                            slice=Name(id='attr', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='int', kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='float', ctx=Load()),
                                                        args=[Name(id='val', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='types',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='attr', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='float', kind=None)],
                                            ),
                                            body=[
                                                Return(
                                                    value=Call(
                                                        func=Name(id='float', ctx=Load()),
                                                        args=[Name(id='val', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Return(
                                                    value=Call(
                                                        func=Name(id='utfstr', ctx=Load()),
                                                        args=[Name(id='val', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='push',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='style', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Dict(keys=[], values=[])],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='push a new level on the stack with a style dictionnary containing style:value pairs', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='_style', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='attr', ctx=Store()),
                            iter=Name(id='style', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='attr', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='cmds',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Compare(
                                                    left=Subscript(
                                                        value=Name(id='style', ctx=Load()),
                                                        slice=Name(id='attr', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    ops=[In()],
                                                    comparators=[
                                                        Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='cmds',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Name(id='attr', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='print', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='WARNING: ESC/POS PRINTING: ignoring invalid value: %s for style %s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Subscript(
                                                                    value=Name(id='style', ctx=Load()),
                                                                    slice=Name(id='attr', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                Call(
                                                                    func=Name(id='utfstr', ctx=Load()),
                                                                    args=[Name(id='attr', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='_style', ctx=Load()),
                                                    slice=Name(id='attr', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='enforce_type',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='attr', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='style', ctx=Load()),
                                                        slice=Name(id='attr', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='stack',
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='_style', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='set',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='style', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Dict(keys=[], values=[])],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='overrides style values at the current stack level', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='_style', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='attr', ctx=Store()),
                            iter=Name(id='style', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='attr', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='cmds',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Compare(
                                                    left=Subscript(
                                                        value=Name(id='style', ctx=Load()),
                                                        slice=Name(id='attr', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    ops=[In()],
                                                    comparators=[
                                                        Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='cmds',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Name(id='attr', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='print', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='WARNING: ESC/POS PRINTING: ignoring invalid value: %s for style %s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Subscript(
                                                                    value=Name(id='style', ctx=Load()),
                                                                    slice=Name(id='attr', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                Name(id='attr', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='stack',
                                                            ctx=Load(),
                                                        ),
                                                        slice=UnaryOp(
                                                            op=USub(),
                                                            operand=Constant(value=1, kind=None),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='attr', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='enforce_type',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='attr', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='style', ctx=Load()),
                                                        slice=Name(id='attr', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='pop',
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
                            value=Constant(value=' pop a style stack level ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='stack',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='stack',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='stack',
                                            ctx=Load(),
                                        ),
                                        slice=Slice(
                                            lower=None,
                                            upper=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                            step=None,
                                        ),
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
                FunctionDef(
                    name='to_escpos',
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
                            value=Constant(value=' converts the current style to an escpos command string ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='cmd', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ordered_cmds', ctx=Store())],
                            value=Call(
                                func=Name(id='sorted', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='cmds',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='x', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Subscript(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='cmds',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='x', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='_order', kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='style', ctx=Store()),
                            iter=Name(id='ordered_cmds', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='cmd', ctx=Store()),
                                    op=Add(),
                                    value=Subscript(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cmds',
                                                ctx=Load(),
                                            ),
                                            slice=Name(id='style', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        slice=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='style', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='cmd', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='XmlSerializer',
            bases=[],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' \n    Converts the xml inline / block tree structure to a string,\n    keeping track of newlines and spacings.\n    The string is outputted asap to the provided escpos driver.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='escpos', annotation=None, type_comment=None),
                        ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='escpos',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='escpos', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='stack',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[Constant(value='block', kind=None)],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='dirty',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='start_inline',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='stylestack', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' starts an inline entity with an optional style definition ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='stack',
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='inline', kind=None)],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='dirty',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='escpos',
                                                ctx=Load(),
                                            ),
                                            attr='_raw',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=' ', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='stylestack', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='style',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='stylestack', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='start_block',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='stylestack', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' starts a block entity with an optional style definition ', kind=None),
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='dirty',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='escpos',
                                                ctx=Load(),
                                            ),
                                            attr='_raw',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='\n', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='dirty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='stack',
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='block', kind=None)],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='stylestack', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='style',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='stylestack', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='end_entity',
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
                            value=Constant(value=' ends the entity definition. (but does not cancel the active style!) ', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='stack',
                                                ctx=Load(),
                                            ),
                                            slice=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='block', kind=None)],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='dirty',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='escpos',
                                                ctx=Load(),
                                            ),
                                            attr='_raw',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='\n', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='dirty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='stack',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='stack',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='stack',
                                            ctx=Load(),
                                        ),
                                        slice=Slice(
                                            lower=None,
                                            upper=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                            step=None,
                                        ),
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
                FunctionDef(
                    name='pre',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='text', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' puts a string of text in the entity keeping the whitespace intact ', kind=None),
                        ),
                        If(
                            test=Name(id='text', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='escpos',
                                                ctx=Load(),
                                            ),
                                            attr='text',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='text', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='dirty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
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
                FunctionDef(
                    name='text',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='text', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' puts text in the entity. Whitespace and newlines are stripped to single spaces. ', kind=None),
                        ),
                        If(
                            test=Name(id='text', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='text', ctx=Store())],
                                    value=Call(
                                        func=Name(id='utfstr', ctx=Load()),
                                        args=[Name(id='text', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='text', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='text', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='text', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='sub',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='\\s+', kind=None),
                                            Constant(value=' ', kind=None),
                                            Name(id='text', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='text', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='dirty',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='escpos',
                                                        ctx=Load(),
                                                    ),
                                                    attr='text',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='text', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='linebreak',
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
                            value=Constant(value=' inserts a linebreak in the entity ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='dirty',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='escpos',
                                        ctx=Load(),
                                    ),
                                    attr='_raw',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='\n', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='style',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='stylestack', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' apply a style to the entity (only applies to content added after the definition) ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='raw',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='stylestack', ctx=Load()),
                                            attr='to_escpos',
                                            ctx=Load(),
                                        ),
                                        args=[],
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
                FunctionDef(
                    name='raw',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='raw', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' puts raw text or escpos command in the entity without affecting the state of the serializer ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='escpos',
                                        ctx=Load(),
                                    ),
                                    attr='_raw',
                                    ctx=Load(),
                                ),
                                args=[Name(id='raw', ctx=Load())],
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
        ClassDef(
            name='XmlLineSerializer',
            bases=[],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' \n    This is used to convert a xml tree into a single line, with a left and a right part.\n    The content is not output to escpos directly, and is intended to be fedback to the\n    XmlSerializer as the content of a block entity.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                            arg(arg='tabwidth', annotation=None, type_comment=None),
                            arg(arg='width', annotation=None, type_comment=None),
                            arg(arg='ratio', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=0, kind=None),
                            Constant(value=2, kind=None),
                            Constant(value=48, kind=None),
                            Constant(value=0.5, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='tabwidth',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='tabwidth', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='indent',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='indent', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='width',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='max', ctx=Load()),
                                args=[
                                    Constant(value=0, kind=None),
                                    BinOp(
                                        left=Name(id='width', ctx=Load()),
                                        op=Sub(),
                                        right=Call(
                                            func=Name(id='int', ctx=Load()),
                                            args=[
                                                BinOp(
                                                    left=Name(id='tabwidth', ctx=Load()),
                                                    op=Mult(),
                                                    right=Name(id='indent', ctx=Load()),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='lwidth',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='width',
                                            ctx=Load(),
                                        ),
                                        op=Mult(),
                                        right=Name(id='ratio', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rwidth',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='max', ctx=Load()),
                                args=[
                                    Constant(value=0, kind=None),
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='width',
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='lwidth',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='clwidth',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='crwidth',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='lbuffer',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rbuffer',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='left',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_txt',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='txt', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='left',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='clwidth',
                                            ctx=Load(),
                                        ),
                                        ops=[Lt()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='lwidth',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='txt', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='txt', ctx=Load()),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Call(
                                                        func=Name(id='max', ctx=Load()),
                                                        args=[
                                                            Constant(value=0, kind=None),
                                                            BinOp(
                                                                left=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='lwidth',
                                                                    ctx=Load(),
                                                                ),
                                                                op=Sub(),
                                                                right=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='clwidth',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='lbuffer',
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Name(id='txt', ctx=Load()),
                                        ),
                                        AugAssign(
                                            target=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='clwidth',
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='txt', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='crwidth',
                                            ctx=Load(),
                                        ),
                                        ops=[Lt()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='rwidth',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='txt', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='txt', ctx=Load()),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Call(
                                                        func=Name(id='max', ctx=Load()),
                                                        args=[
                                                            Constant(value=0, kind=None),
                                                            BinOp(
                                                                left=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='rwidth',
                                                                    ctx=Load(),
                                                                ),
                                                                op=Sub(),
                                                                right=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='crwidth',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='rbuffer',
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Name(id='txt', ctx=Load()),
                                        ),
                                        AugAssign(
                                            target=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='crwidth',
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='txt', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='start_inline',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='stylestack', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='left',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='clwidth',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='left',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='crwidth',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_txt',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=' ', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='start_block',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='stylestack', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='start_inline',
                                    ctx=Load(),
                                ),
                                args=[Name(id='stylestack', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='end_entity',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[Pass()],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='pre',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='text', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Name(id='text', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_txt',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='text', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='text',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='text', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Name(id='text', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='text', ctx=Store())],
                                    value=Call(
                                        func=Name(id='utfstr', ctx=Load()),
                                        args=[Name(id='text', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='text', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='text', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='text', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='sub',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='\\s+', kind=None),
                                            Constant(value=' ', kind=None),
                                            Name(id='text', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='text', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_txt',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='text', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='linebreak',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[Pass()],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='style',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='stylestack', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[Pass()],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='raw',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='raw', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[Pass()],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='start_right',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='left',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_line',
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
                        Return(
                            value=BinOp(
                                left=BinOp(
                                    left=BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=Constant(value=' ', kind=None),
                                                op=Mult(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='indent',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            op=Mult(),
                                            right=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tabwidth',
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='lbuffer',
                                            ctx=Load(),
                                        ),
                                    ),
                                    op=Add(),
                                    right=BinOp(
                                        left=Constant(value=' ', kind=None),
                                        op=Mult(),
                                        right=BinOp(
                                            left=BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='width',
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='clwidth',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            op=Sub(),
                                            right=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='crwidth',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rbuffer',
                                    ctx=Load(),
                                ),
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
        ClassDef(
            name='Escpos',
            bases=[],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' ESC/POS Printer object ', kind=None),
                ),
                Assign(
                    targets=[Name(id='device', ctx=Store())],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='encoding', ctx=Store())],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='img_cache', ctx=Store())],
                    value=Dict(keys=[], values=[]),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_image_size',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='size', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Check and fix the size of the image to 32 bits ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=BinOp(
                                    left=Name(id='size', ctx=Load()),
                                    op=Mod(),
                                    right=Constant(value=32, kind=None),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='image_border', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value=32, kind=None),
                                        op=Sub(),
                                        right=BinOp(
                                            left=Name(id='size', ctx=Load()),
                                            op=Mod(),
                                            right=Constant(value=32, kind=None),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=BinOp(
                                            left=Name(id='image_border', ctx=Load()),
                                            op=Mod(),
                                            right=Constant(value=2, kind=None),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Name(id='image_border', ctx=Load()),
                                                                op=Div(),
                                                                right=Constant(value=2, kind=None),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Name(id='image_border', ctx=Load()),
                                                                op=Div(),
                                                                right=Constant(value=2, kind=None),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Name(id='image_border', ctx=Load()),
                                                                op=Div(),
                                                                right=Constant(value=2, kind=None),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=BinOp(
                                                                    left=Name(id='image_border', ctx=Load()),
                                                                    op=Div(),
                                                                    right=Constant(value=2, kind=None),
                                                                ),
                                                                op=Add(),
                                                                right=Constant(value=1, kind=None),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_print_image',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='line', annotation=None, type_comment=None),
                            arg(arg='size', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Print formatted image ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='i', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cont', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='buffer', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_raw',
                                    ctx=Load(),
                                ),
                                args=[Name(id='S_RASTER_N', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='buffer', ctx=Store())],
                            value=BinOp(
                                left=Constant(value=b'%02X%02X%02X%02X', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Call(
                                            func=Name(id='int', ctx=Load()),
                                            args=[
                                                BinOp(
                                                    left=BinOp(
                                                        left=Subscript(
                                                            value=Name(id='size', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        op=Div(),
                                                        right=Subscript(
                                                            value=Name(id='size', ctx=Load()),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    op=Div(),
                                                    right=Constant(value=8, kind=None),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        Constant(value=0, kind=None),
                                        Subscript(
                                            value=Name(id='size', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        Constant(value=0, kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_raw',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='codecs', ctx=Load()),
                                            attr='decode',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='buffer', ctx=Load()),
                                            Constant(value='hex', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='buffer', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        While(
                            test=Compare(
                                left=Name(id='i', ctx=Load()),
                                ops=[Lt()],
                                comparators=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='line', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='hex_string', ctx=Store())],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='line', ctx=Load()),
                                                slice=Slice(
                                                    lower=Name(id='i', ctx=Load()),
                                                    upper=BinOp(
                                                        left=Name(id='i', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value=8, kind=None),
                                                    ),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='buffer', ctx=Store()),
                                    op=Add(),
                                    value=BinOp(
                                        left=Constant(value='%02X', kind=None),
                                        op=Mod(),
                                        right=Name(id='hex_string', ctx=Load()),
                                    ),
                                ),
                                AugAssign(
                                    target=Name(id='i', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=8, kind=None),
                                ),
                                AugAssign(
                                    target=Name(id='cont', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                                If(
                                    test=Compare(
                                        left=BinOp(
                                            left=Name(id='cont', ctx=Load()),
                                            op=Mod(),
                                            right=Constant(value=4, kind=None),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_raw',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='codecs', ctx=Load()),
                                                            attr='decode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='buffer', ctx=Load()),
                                                            Constant(value='hex', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='buffer', ctx=Store())],
                                            value=Constant(value='', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='cont', ctx=Store())],
                                            value=Constant(value=0, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_raw_print_image',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='line', annotation=None, type_comment=None),
                            arg(arg='size', annotation=None, type_comment=None),
                            arg(arg='output', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Print formatted image ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='i', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cont', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='buffer', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='raw', ctx=Store())],
                            value=Constant(value=b'', kind=None),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='__raw',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='string', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=Name(id='output', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='output', ctx=Load()),
                                                args=[Name(id='string', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_raw',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='string', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Name(id='raw', ctx=Store()),
                            op=Add(),
                            value=Call(
                                func=Attribute(
                                    value=Name(id='S_RASTER_N', ctx=Load()),
                                    attr='encode',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='utf-8', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='buffer', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='%02X%02X%02X%02X', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Call(
                                            func=Name(id='int', ctx=Load()),
                                            args=[
                                                BinOp(
                                                    left=BinOp(
                                                        left=Subscript(
                                                            value=Name(id='size', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        op=Div(),
                                                        right=Subscript(
                                                            value=Name(id='size', ctx=Load()),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    op=Div(),
                                                    right=Constant(value=8, kind=None),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        Constant(value=0, kind=None),
                                        Subscript(
                                            value=Name(id='size', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        Constant(value=0, kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Name(id='raw', ctx=Store()),
                            op=Add(),
                            value=Call(
                                func=Attribute(
                                    value=Name(id='codecs', ctx=Load()),
                                    attr='decode',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='buffer', ctx=Load()),
                                    Constant(value='hex', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='buffer', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        While(
                            test=Compare(
                                left=Name(id='i', ctx=Load()),
                                ops=[Lt()],
                                comparators=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='line', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='hex_string', ctx=Store())],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='line', ctx=Load()),
                                                slice=Slice(
                                                    lower=Name(id='i', ctx=Load()),
                                                    upper=BinOp(
                                                        left=Name(id='i', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value=8, kind=None),
                                                    ),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='buffer', ctx=Store()),
                                    op=Add(),
                                    value=BinOp(
                                        left=Constant(value='%02X', kind=None),
                                        op=Mod(),
                                        right=Name(id='hex_string', ctx=Load()),
                                    ),
                                ),
                                AugAssign(
                                    target=Name(id='i', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=8, kind=None),
                                ),
                                AugAssign(
                                    target=Name(id='cont', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                                If(
                                    test=Compare(
                                        left=BinOp(
                                            left=Name(id='cont', ctx=Load()),
                                            op=Mod(),
                                            right=Constant(value=4, kind=None),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='raw', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='codecs', ctx=Load()),
                                                    attr='decode',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='buffer', ctx=Load()),
                                                    Constant(value='hex', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='buffer', ctx=Store())],
                                            value=Constant(value='', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='cont', ctx=Store())],
                                            value=Constant(value=0, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='raw', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_convert_image',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='im', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Parse image and prepare it to a printable format ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='pixels', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pix_line', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='im_left', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='im_right', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='switch', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='img_size', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Attribute(
                                        value=Name(id='im', ctx=Load()),
                                        attr='size',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=512, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='print', ctx=Load()),
                                        args=[Constant(value='WARNING: Image is wider than 512 and could be truncated at print time ', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Attribute(
                                        value=Name(id='im', ctx=Load()),
                                        attr='size',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value=1, kind=None),
                                    ctx=Load(),
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=255, kind=None)],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ImageSizeError', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='im_border', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_image_size',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='im', ctx=Load()),
                                            attr='size',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Name(id='im_border', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='im_left', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value='0', kind=None),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Name(id='im_border', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='im_right', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value='0', kind=None),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='y', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='im', ctx=Load()),
                                            attr='size',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='img_size', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                                AugAssign(
                                    target=Name(id='pix_line', ctx=Store()),
                                    op=Add(),
                                    value=Name(id='im_left', ctx=Load()),
                                ),
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='img_size', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Subscript(
                                        value=Name(id='im_border', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                                For(
                                    target=Name(id='x', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='im', ctx=Load()),
                                                    attr='size',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='img_size', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Constant(value=1, kind=None),
                                        ),
                                        Assign(
                                            targets=[Name(id='RGB', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='im', ctx=Load()),
                                                    attr='getpixel',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='x', ctx=Load()),
                                                            Name(id='y', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='im_color', ctx=Store())],
                                            value=BinOp(
                                                left=BinOp(
                                                    left=Subscript(
                                                        value=Name(id='RGB', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    op=Add(),
                                                    right=Subscript(
                                                        value=Name(id='RGB', ctx=Load()),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Subscript(
                                                    value=Name(id='RGB', ctx=Load()),
                                                    slice=Constant(value=2, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='im_pattern', ctx=Store())],
                                            value=Constant(value='1X0', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='pattern_len', ctx=Store())],
                                            value=Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='im_pattern', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='switch', ctx=Store())],
                                            value=BinOp(
                                                left=BinOp(
                                                    left=Name(id='switch', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                                op=Mult(),
                                                right=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='x', ctx=Store()),
                                            iter=Call(
                                                func=Name(id='range', ctx=Load()),
                                                args=[Name(id='pattern_len', ctx=Load())],
                                                keywords=[],
                                            ),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='im_color', ctx=Load()),
                                                        ops=[LtE()],
                                                        comparators=[
                                                            BinOp(
                                                                left=BinOp(
                                                                    left=BinOp(
                                                                        left=Constant(value=255, kind=None),
                                                                        op=Mult(),
                                                                        right=Constant(value=3, kind=None),
                                                                    ),
                                                                    op=Div(),
                                                                    right=Name(id='pattern_len', ctx=Load()),
                                                                ),
                                                                op=Mult(),
                                                                right=BinOp(
                                                                    left=Name(id='x', ctx=Load()),
                                                                    op=Add(),
                                                                    right=Constant(value=1, kind=None),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        If(
                                                            test=Compare(
                                                                left=Subscript(
                                                                    value=Name(id='im_pattern', ctx=Load()),
                                                                    slice=Name(id='x', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='X', kind=None)],
                                                            ),
                                                            body=[
                                                                AugAssign(
                                                                    target=Name(id='pix_line', ctx=Store()),
                                                                    op=Add(),
                                                                    value=BinOp(
                                                                        left=Constant(value='%d', kind=None),
                                                                        op=Mod(),
                                                                        right=Name(id='switch', ctx=Load()),
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                AugAssign(
                                                                    target=Name(id='pix_line', ctx=Store()),
                                                                    op=Add(),
                                                                    value=Subscript(
                                                                        value=Name(id='im_pattern', ctx=Load()),
                                                                        slice=Name(id='x', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        Break(),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Name(id='im_color', ctx=Load()),
                                                                        ops=[Gt()],
                                                                        comparators=[
                                                                            BinOp(
                                                                                left=BinOp(
                                                                                    left=BinOp(
                                                                                        left=Constant(value=255, kind=None),
                                                                                        op=Mult(),
                                                                                        right=Constant(value=3, kind=None),
                                                                                    ),
                                                                                    op=Div(),
                                                                                    right=Name(id='pattern_len', ctx=Load()),
                                                                                ),
                                                                                op=Mult(),
                                                                                right=Name(id='pattern_len', ctx=Load()),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    Compare(
                                                                        left=Name(id='im_color', ctx=Load()),
                                                                        ops=[LtE()],
                                                                        comparators=[
                                                                            BinOp(
                                                                                left=Constant(value=255, kind=None),
                                                                                op=Mult(),
                                                                                right=Constant(value=3, kind=None),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                AugAssign(
                                                                    target=Name(id='pix_line', ctx=Store()),
                                                                    op=Add(),
                                                                    value=Subscript(
                                                                        value=Name(id='im_pattern', ctx=Load()),
                                                                        slice=UnaryOp(
                                                                            op=USub(),
                                                                            operand=Constant(value=1, kind=None),
                                                                        ),
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                Break(),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='pix_line', ctx=Store()),
                                    op=Add(),
                                    value=Name(id='im_right', ctx=Load()),
                                ),
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='img_size', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Subscript(
                                        value=Name(id='im_border', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='pix_line', ctx=Load()),
                                    Name(id='img_size', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='image',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='path_img', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Open image file ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='im_open', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Image', ctx=Load()),
                                    attr='open',
                                    ctx=Load(),
                                ),
                                args=[Name(id='path_img', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='im', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='im_open', ctx=Load()),
                                    attr='convert',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='RGB', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='pix_line', ctx=Store()),
                                        Name(id='img_size', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_convert_image',
                                    ctx=Load(),
                                ),
                                args=[Name(id='im', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_print_image',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='pix_line', ctx=Load()),
                                    Name(id='img_size', ctx=Load()),
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
                    name='print_base64_image',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='img', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='print', ctx=Load()),
                                args=[Constant(value='print_b64_img', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='md5', ctx=Load()),
                                        args=[Name(id='img', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='digest',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='id', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='img_cache',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='print', ctx=Load()),
                                        args=[Constant(value='not in cache', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='img', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='img', ctx=Load()),
                                        slice=Slice(
                                            lower=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='img', ctx=Load()),
                                                        attr='find',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value=b',', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                            upper=None,
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='f', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='io', ctx=Load()),
                                            attr='BytesIO',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=b'img', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='f', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='base64', ctx=Load()),
                                                    attr='decodebytes',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='img', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='f', ctx=Load()),
                                            attr='seek',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0, kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='img_rgba', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Image', ctx=Load()),
                                            attr='open',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='f', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='img', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Image', ctx=Load()),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='RGB', kind=None),
                                            Attribute(
                                                value=Name(id='img_rgba', ctx=Load()),
                                                attr='size',
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=255, kind=None),
                                                    Constant(value=255, kind=None),
                                                    Constant(value=255, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='channels', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='img_rgba', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='channels', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=3, kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='img', ctx=Load()),
                                                    attr='paste',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='img_rgba', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='mask',
                                                        value=Subscript(
                                                            value=Name(id='channels', ctx=Load()),
                                                            slice=Constant(value=3, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='img', ctx=Load()),
                                                    attr='paste',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='img_rgba', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='print', ctx=Load()),
                                        args=[Constant(value='convert image', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='pix_line', ctx=Store()),
                                                Name(id='img_size', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_convert_image',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='img', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='print', ctx=Load()),
                                        args=[Constant(value='print image', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='buffer', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raw_print_image',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='pix_line', ctx=Load()),
                                            Name(id='img_size', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='img_cache',
                                                ctx=Load(),
                                            ),
                                            slice=Name(id='id', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='buffer', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='print', ctx=Load()),
                                args=[Constant(value='raw image', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_raw',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='img_cache',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='id', ctx=Load()),
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
                FunctionDef(
                    name='qr',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='text', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Print QR Code for the provided string ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='qr_code', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='qrcode', ctx=Load()),
                                    attr='QRCode',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='version',
                                        value=Constant(value=4, kind=None),
                                    ),
                                    keyword(
                                        arg='box_size',
                                        value=Constant(value=4, kind=None),
                                    ),
                                    keyword(
                                        arg='border',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='qr_code', ctx=Load()),
                                    attr='add_data',
                                    ctx=Load(),
                                ),
                                args=[Name(id='text', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='qr_code', ctx=Load()),
                                    attr='make',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='fit',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='qr_img', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='qr_code', ctx=Load()),
                                    attr='make_image',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='im', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='qr_img', ctx=Load()),
                                        attr='_img',
                                        ctx=Load(),
                                    ),
                                    attr='convert',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='RGB', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_convert_image',
                                    ctx=Load(),
                                ),
                                args=[Name(id='im', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='barcode',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='code', annotation=None, type_comment=None),
                            arg(arg='bc', annotation=None, type_comment=None),
                            arg(arg='width', annotation=None, type_comment=None),
                            arg(arg='height', annotation=None, type_comment=None),
                            arg(arg='pos', annotation=None, type_comment=None),
                            arg(arg='font', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=255, kind=None),
                            Constant(value=2, kind=None),
                            Constant(value='below', kind=None),
                            Constant(value='a', kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Print Barcode ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_raw',
                                    ctx=Load(),
                                ),
                                args=[Name(id='TXT_ALIGN_CT', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Name(id='height', ctx=Load()),
                                        ops=[GtE()],
                                        comparators=[Constant(value=2, kind=None)],
                                    ),
                                    Compare(
                                        left=Name(id='height', ctx=Load()),
                                        ops=[LtE()],
                                        comparators=[Constant(value=6, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raw',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='BARCODE_HEIGHT', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='BarcodeSizeError', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Name(id='width', ctx=Load()),
                                        ops=[GtE()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    Compare(
                                        left=Name(id='width', ctx=Load()),
                                        ops=[LtE()],
                                        comparators=[Constant(value=255, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raw',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='BARCODE_WIDTH', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='BarcodeSizeError', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='font', ctx=Load()),
                                        attr='upper',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='B', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raw',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='BARCODE_FONT_B', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raw',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='BARCODE_FONT_A', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='pos', ctx=Load()),
                                        attr='upper',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='OFF', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raw',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='BARCODE_TXT_OFF', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='pos', ctx=Load()),
                                                attr='upper',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='BOTH', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_raw',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='BARCODE_TXT_BTH', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='pos', ctx=Load()),
                                                        attr='upper',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='ABOVE', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_raw',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='BARCODE_TXT_ABV', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_raw',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='BARCODE_TXT_BLW', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='bc', ctx=Load()),
                                        attr='upper',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='UPC-A', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raw',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='BARCODE_UPC_A', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='bc', ctx=Load()),
                                                attr='upper',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='UPC-E', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_raw',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='BARCODE_UPC_E', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='bc', ctx=Load()),
                                                        attr='upper',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='EAN13', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_raw',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='BARCODE_EAN13', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='bc', ctx=Load()),
                                                                attr='upper',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='EAN8', kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_raw',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='BARCODE_EAN8', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='bc', ctx=Load()),
                                                                        attr='upper',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='CODE39', kind=None)],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_raw',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='BARCODE_CODE39', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='bc', ctx=Load()),
                                                                                attr='upper',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='ITF', kind=None)],
                                                                    ),
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='_raw',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='BARCODE_ITF', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='bc', ctx=Load()),
                                                                                        attr='upper',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[],
                                                                                    keywords=[],
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='NW7', kind=None)],
                                                                            ),
                                                                            body=[
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_raw',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Name(id='BARCODE_NW7', ctx=Load())],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                Raise(
                                                                                    exc=Call(
                                                                                        func=Name(id='BarcodeTypeError', ctx=Load()),
                                                                                        args=[],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    cause=None,
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        If(
                            test=Name(id='code', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raw',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='code', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raw',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='\x00', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='BarcodeCodeError', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='receipt',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='xml', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Prints an xml based receipt definition\n        ', kind=None),
                        ),
                        FunctionDef(
                            name='strclean',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='string', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='string', ctx=Load()),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='string', ctx=Store())],
                                            value=Constant(value='', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='string', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='string', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='string', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='sub',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='\\s+', kind=None),
                                            Constant(value=' ', kind=None),
                                            Name(id='string', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Name(id='string', ctx=Load()),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='format_value',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='value', annotation=None, type_comment=None),
                                    arg(arg='decimals', annotation=None, type_comment=None),
                                    arg(arg='width', annotation=None, type_comment=None),
                                    arg(arg='decimals_separator', annotation=None, type_comment=None),
                                    arg(arg='thousands_separator', annotation=None, type_comment=None),
                                    arg(arg='autoint', annotation=None, type_comment=None),
                                    arg(arg='symbol', annotation=None, type_comment=None),
                                    arg(arg='position', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[
                                    Constant(value=3, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value='.', kind=None),
                                    Constant(value=',', kind=None),
                                    Constant(value=False, kind=None),
                                    Constant(value='', kind=None),
                                    Constant(value='after', kind=None),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='decimals', ctx=Store())],
                                    value=Call(
                                        func=Name(id='max', ctx=Load()),
                                        args=[
                                            Constant(value=0, kind=None),
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[Name(id='decimals', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='width', ctx=Store())],
                                    value=Call(
                                        func=Name(id='max', ctx=Load()),
                                        args=[
                                            Constant(value=0, kind=None),
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[Name(id='width', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='value', ctx=Store())],
                                    value=Call(
                                        func=Name(id='float', ctx=Load()),
                                        args=[Name(id='value', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='autoint', ctx=Load()),
                                            Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='math', ctx=Load()),
                                                        attr='floor',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='value', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Name(id='value', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='decimals', ctx=Store())],
                                            value=Constant(value=0, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='width', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='width', ctx=Store())],
                                            value=Constant(value='', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Name(id='thousands_separator', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='formatstr', ctx=Store())],
                                            value=BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=BinOp(
                                                            left=Constant(value='{:', kind=None),
                                                            op=Add(),
                                                            right=Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[Name(id='width', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        op=Add(),
                                                        right=Constant(value=',.', kind=None),
                                                    ),
                                                    op=Add(),
                                                    right=Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='decimals', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Constant(value='f}', kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='formatstr', ctx=Store())],
                                            value=BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=BinOp(
                                                            left=Constant(value='{:', kind=None),
                                                            op=Add(),
                                                            right=Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[Name(id='width', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        op=Add(),
                                                        right=Constant(value='.', kind=None),
                                                    ),
                                                    op=Add(),
                                                    right=Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='decimals', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Constant(value='f}', kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='ret', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='formatstr', ctx=Load()),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='value', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='ret', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='ret', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=',', kind=None),
                                            Constant(value='COMMA', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='ret', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='ret', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='.', kind=None),
                                            Constant(value='DOT', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='ret', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='ret', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='COMMA', kind=None),
                                            Name(id='thousands_separator', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='ret', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='ret', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='DOT', kind=None),
                                            Name(id='decimals_separator', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='symbol', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='position', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='after', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='ret', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='ret', ctx=Load()),
                                                        op=Add(),
                                                        right=Name(id='symbol', ctx=Load()),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='ret', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='symbol', ctx=Load()),
                                                        op=Add(),
                                                        right=Name(id='ret', ctx=Load()),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Name(id='ret', ctx=Load()),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='print_elem',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='stylestack', annotation=None, type_comment=None),
                                    arg(arg='serializer', annotation=None, type_comment=None),
                                    arg(arg='elem', annotation=None, type_comment=None),
                                    arg(arg='indent', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='elem_styles', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='h1', kind=None),
                                            Constant(value='h2', kind=None),
                                            Constant(value='h3', kind=None),
                                            Constant(value='h4', kind=None),
                                            Constant(value='h5', kind=None),
                                            Constant(value='em', kind=None),
                                            Constant(value='b', kind=None),
                                        ],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='bold', kind=None),
                                                    Constant(value='size', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='on', kind=None),
                                                    Constant(value='double', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[Constant(value='size', kind=None)],
                                                values=[Constant(value='double', kind=None)],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='bold', kind=None),
                                                    Constant(value='size', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='on', kind=None),
                                                    Constant(value='double-height', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[Constant(value='size', kind=None)],
                                                values=[Constant(value='double-height', kind=None)],
                                            ),
                                            Dict(
                                                keys=[Constant(value='bold', kind=None)],
                                                values=[Constant(value='on', kind=None)],
                                            ),
                                            Dict(
                                                keys=[Constant(value='font', kind=None)],
                                                values=[Constant(value='b', kind=None)],
                                            ),
                                            Dict(
                                                keys=[Constant(value='bold', kind=None)],
                                                values=[Constant(value='on', kind=None)],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='stylestack', ctx=Load()),
                                            attr='push',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='elem', ctx=Load()),
                                            attr='tag',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[Name(id='elem_styles', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='stylestack', ctx=Load()),
                                                    attr='set',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='elem_styles', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='elem', ctx=Load()),
                                                            attr='tag',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='stylestack', ctx=Load()),
                                            attr='set',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='elem', ctx=Load()),
                                                attr='attrib',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='elem', ctx=Load()),
                                            attr='tag',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='p', kind=None),
                                                    Constant(value='div', kind=None),
                                                    Constant(value='section', kind=None),
                                                    Constant(value='article', kind=None),
                                                    Constant(value='receipt', kind=None),
                                                    Constant(value='header', kind=None),
                                                    Constant(value='footer', kind=None),
                                                    Constant(value='li', kind=None),
                                                    Constant(value='h1', kind=None),
                                                    Constant(value='h2', kind=None),
                                                    Constant(value='h3', kind=None),
                                                    Constant(value='h4', kind=None),
                                                    Constant(value='h5', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='serializer', ctx=Load()),
                                                    attr='start_block',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='stylestack', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='serializer', ctx=Load()),
                                                    attr='text',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='elem', ctx=Load()),
                                                        attr='text',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        For(
                                            target=Name(id='child', ctx=Store()),
                                            iter=Name(id='elem', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='print_elem', ctx=Load()),
                                                        args=[
                                                            Name(id='stylestack', ctx=Load()),
                                                            Name(id='serializer', ctx=Load()),
                                                            Name(id='child', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='serializer', ctx=Load()),
                                                            attr='start_inline',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='stylestack', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='serializer', ctx=Load()),
                                                            attr='text',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='child', ctx=Load()),
                                                                attr='tail',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='serializer', ctx=Load()),
                                                            attr='end_entity',
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
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='serializer', ctx=Load()),
                                                    attr='end_entity',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='elem', ctx=Load()),
                                                    attr='tag',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='span', kind=None),
                                                            Constant(value='em', kind=None),
                                                            Constant(value='b', kind=None),
                                                            Constant(value='left', kind=None),
                                                            Constant(value='right', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='serializer', ctx=Load()),
                                                            attr='start_inline',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='stylestack', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='serializer', ctx=Load()),
                                                            attr='text',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='elem', ctx=Load()),
                                                                attr='text',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                For(
                                                    target=Name(id='child', ctx=Store()),
                                                    iter=Name(id='elem', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Name(id='print_elem', ctx=Load()),
                                                                args=[
                                                                    Name(id='stylestack', ctx=Load()),
                                                                    Name(id='serializer', ctx=Load()),
                                                                    Name(id='child', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='serializer', ctx=Load()),
                                                                    attr='start_inline',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='stylestack', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='serializer', ctx=Load()),
                                                                    attr='text',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='child', ctx=Load()),
                                                                        attr='tail',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='serializer', ctx=Load()),
                                                                    attr='end_entity',
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
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='serializer', ctx=Load()),
                                                            attr='end_entity',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='elem', ctx=Load()),
                                                            attr='tag',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='value', kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='serializer', ctx=Load()),
                                                                    attr='start_inline',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='stylestack', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='serializer', ctx=Load()),
                                                                    attr='pre',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='format_value', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='elem', ctx=Load()),
                                                                                attr='text',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='decimals',
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='stylestack', ctx=Load()),
                                                                                        attr='get',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Constant(value='value-decimals', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                            ),
                                                                            keyword(
                                                                                arg='width',
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='stylestack', ctx=Load()),
                                                                                        attr='get',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Constant(value='value-width', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                            ),
                                                                            keyword(
                                                                                arg='decimals_separator',
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='stylestack', ctx=Load()),
                                                                                        attr='get',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Constant(value='value-decimals-separator', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                            ),
                                                                            keyword(
                                                                                arg='thousands_separator',
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='stylestack', ctx=Load()),
                                                                                        attr='get',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Constant(value='value-thousands-separator', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                            ),
                                                                            keyword(
                                                                                arg='autoint',
                                                                                value=Compare(
                                                                                    left=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='stylestack', ctx=Load()),
                                                                                            attr='get',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='value-autoint', kind=None)],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    ops=[Eq()],
                                                                                    comparators=[Constant(value='on', kind=None)],
                                                                                ),
                                                                            ),
                                                                            keyword(
                                                                                arg='symbol',
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='stylestack', ctx=Load()),
                                                                                        attr='get',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Constant(value='value-symbol', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                            ),
                                                                            keyword(
                                                                                arg='position',
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='stylestack', ctx=Load()),
                                                                                        attr='get',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Constant(value='value-symbol-position', kind=None)],
                                                                                    keywords=[],
                                                                                ),
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
                                                                    value=Name(id='serializer', ctx=Load()),
                                                                    attr='end_entity',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='elem', ctx=Load()),
                                                                    attr='tag',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='line', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='width', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='stylestack', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='width', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Compare(
                                                                        left=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='stylestack', ctx=Load()),
                                                                                attr='get',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Constant(value='size', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        ops=[In()],
                                                                        comparators=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='double', kind=None),
                                                                                    Constant(value='double-width', kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='width', ctx=Store())],
                                                                            value=BinOp(
                                                                                left=Name(id='width', ctx=Load()),
                                                                                op=Div(),
                                                                                right=Constant(value=2, kind=None),
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='lineserializer', ctx=Store())],
                                                                    value=Call(
                                                                        func=Name(id='XmlLineSerializer', ctx=Load()),
                                                                        args=[
                                                                            BinOp(
                                                                                left=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='stylestack', ctx=Load()),
                                                                                        attr='get',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Constant(value='indent', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                                op=Add(),
                                                                                right=Name(id='indent', ctx=Load()),
                                                                            ),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='stylestack', ctx=Load()),
                                                                                    attr='get',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='tabwidth', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                            Name(id='width', ctx=Load()),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='stylestack', ctx=Load()),
                                                                                    attr='get',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='line-ratio', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='serializer', ctx=Load()),
                                                                            attr='start_block',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='stylestack', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                For(
                                                                    target=Name(id='child', ctx=Store()),
                                                                    iter=Name(id='elem', ctx=Load()),
                                                                    body=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Attribute(
                                                                                    value=Name(id='child', ctx=Load()),
                                                                                    attr='tag',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='left', kind=None)],
                                                                            ),
                                                                            body=[
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Name(id='print_elem', ctx=Load()),
                                                                                        args=[
                                                                                            Name(id='stylestack', ctx=Load()),
                                                                                            Name(id='lineserializer', ctx=Load()),
                                                                                            Name(id='child', ctx=Load()),
                                                                                        ],
                                                                                        keywords=[
                                                                                            keyword(
                                                                                                arg='indent',
                                                                                                value=Name(id='indent', ctx=Load()),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                If(
                                                                                    test=Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='child', ctx=Load()),
                                                                                            attr='tag',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[Constant(value='right', kind=None)],
                                                                                    ),
                                                                                    body=[
                                                                                        Expr(
                                                                                            value=Call(
                                                                                                func=Attribute(
                                                                                                    value=Name(id='lineserializer', ctx=Load()),
                                                                                                    attr='start_right',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ),
                                                                                        Expr(
                                                                                            value=Call(
                                                                                                func=Name(id='print_elem', ctx=Load()),
                                                                                                args=[
                                                                                                    Name(id='stylestack', ctx=Load()),
                                                                                                    Name(id='lineserializer', ctx=Load()),
                                                                                                    Name(id='child', ctx=Load()),
                                                                                                ],
                                                                                                keywords=[
                                                                                                    keyword(
                                                                                                        arg='indent',
                                                                                                        value=Name(id='indent', ctx=Load()),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                    type_comment=None,
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='serializer', ctx=Load()),
                                                                            attr='pre',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='lineserializer', ctx=Load()),
                                                                                    attr='get_line',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='serializer', ctx=Load()),
                                                                            attr='end_entity',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='elem', ctx=Load()),
                                                                            attr='tag',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='ul', kind=None)],
                                                                    ),
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='serializer', ctx=Load()),
                                                                                    attr='start_block',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='stylestack', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                        Assign(
                                                                            targets=[Name(id='bullet', ctx=Store())],
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='stylestack', ctx=Load()),
                                                                                    attr='get',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='bullet', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        For(
                                                                            target=Name(id='child', ctx=Store()),
                                                                            iter=Name(id='elem', ctx=Load()),
                                                                            body=[
                                                                                If(
                                                                                    test=Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='child', ctx=Load()),
                                                                                            attr='tag',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[Constant(value='li', kind=None)],
                                                                                    ),
                                                                                    body=[
                                                                                        Expr(
                                                                                            value=Call(
                                                                                                func=Attribute(
                                                                                                    value=Name(id='serializer', ctx=Load()),
                                                                                                    attr='style',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[Name(id='stylestack', ctx=Load())],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ),
                                                                                        Expr(
                                                                                            value=Call(
                                                                                                func=Attribute(
                                                                                                    value=Name(id='serializer', ctx=Load()),
                                                                                                    attr='raw',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[
                                                                                                    BinOp(
                                                                                                        left=BinOp(
                                                                                                            left=BinOp(
                                                                                                                left=Constant(value=' ', kind=None),
                                                                                                                op=Mult(),
                                                                                                                right=Name(id='indent', ctx=Load()),
                                                                                                            ),
                                                                                                            op=Mult(),
                                                                                                            right=Call(
                                                                                                                func=Attribute(
                                                                                                                    value=Name(id='stylestack', ctx=Load()),
                                                                                                                    attr='get',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                args=[Constant(value='tabwidth', kind=None)],
                                                                                                                keywords=[],
                                                                                                            ),
                                                                                                        ),
                                                                                                        op=Add(),
                                                                                                        right=Name(id='bullet', ctx=Load()),
                                                                                                    ),
                                                                                                ],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[],
                                                                                ),
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Name(id='print_elem', ctx=Load()),
                                                                                        args=[
                                                                                            Name(id='stylestack', ctx=Load()),
                                                                                            Name(id='serializer', ctx=Load()),
                                                                                            Name(id='child', ctx=Load()),
                                                                                        ],
                                                                                        keywords=[
                                                                                            keyword(
                                                                                                arg='indent',
                                                                                                value=BinOp(
                                                                                                    left=Name(id='indent', ctx=Load()),
                                                                                                    op=Add(),
                                                                                                    right=Constant(value=1, kind=None),
                                                                                                ),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[],
                                                                            type_comment=None,
                                                                        ),
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='serializer', ctx=Load()),
                                                                                    attr='end_entity',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Attribute(
                                                                                    value=Name(id='elem', ctx=Load()),
                                                                                    attr='tag',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='ol', kind=None)],
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='cwidth', ctx=Store())],
                                                                                    value=BinOp(
                                                                                        left=Call(
                                                                                            func=Name(id='len', ctx=Load()),
                                                                                            args=[
                                                                                                Call(
                                                                                                    func=Name(id='str', ctx=Load()),
                                                                                                    args=[
                                                                                                        Call(
                                                                                                            func=Name(id='len', ctx=Load()),
                                                                                                            args=[Name(id='elem', ctx=Load())],
                                                                                                            keywords=[],
                                                                                                        ),
                                                                                                    ],
                                                                                                    keywords=[],
                                                                                                ),
                                                                                            ],
                                                                                            keywords=[],
                                                                                        ),
                                                                                        op=Add(),
                                                                                        right=Constant(value=2, kind=None),
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                                Assign(
                                                                                    targets=[Name(id='i', ctx=Store())],
                                                                                    value=Constant(value=1, kind=None),
                                                                                    type_comment=None,
                                                                                ),
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='serializer', ctx=Load()),
                                                                                            attr='start_block',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Name(id='stylestack', ctx=Load())],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                                For(
                                                                                    target=Name(id='child', ctx=Store()),
                                                                                    iter=Name(id='elem', ctx=Load()),
                                                                                    body=[
                                                                                        If(
                                                                                            test=Compare(
                                                                                                left=Attribute(
                                                                                                    value=Name(id='child', ctx=Load()),
                                                                                                    attr='tag',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[Constant(value='li', kind=None)],
                                                                                            ),
                                                                                            body=[
                                                                                                Expr(
                                                                                                    value=Call(
                                                                                                        func=Attribute(
                                                                                                            value=Name(id='serializer', ctx=Load()),
                                                                                                            attr='style',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        args=[Name(id='stylestack', ctx=Load())],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                ),
                                                                                                Expr(
                                                                                                    value=Call(
                                                                                                        func=Attribute(
                                                                                                            value=Name(id='serializer', ctx=Load()),
                                                                                                            attr='raw',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        args=[
                                                                                                            BinOp(
                                                                                                                left=BinOp(
                                                                                                                    left=BinOp(
                                                                                                                        left=BinOp(
                                                                                                                            left=Constant(value=' ', kind=None),
                                                                                                                            op=Mult(),
                                                                                                                            right=Name(id='indent', ctx=Load()),
                                                                                                                        ),
                                                                                                                        op=Mult(),
                                                                                                                        right=Call(
                                                                                                                            func=Attribute(
                                                                                                                                value=Name(id='stylestack', ctx=Load()),
                                                                                                                                attr='get',
                                                                                                                                ctx=Load(),
                                                                                                                            ),
                                                                                                                            args=[Constant(value='tabwidth', kind=None)],
                                                                                                                            keywords=[],
                                                                                                                        ),
                                                                                                                    ),
                                                                                                                    op=Add(),
                                                                                                                    right=Constant(value=' ', kind=None),
                                                                                                                ),
                                                                                                                op=Add(),
                                                                                                                right=Call(
                                                                                                                    func=Attribute(
                                                                                                                        value=BinOp(
                                                                                                                            left=Call(
                                                                                                                                func=Name(id='str', ctx=Load()),
                                                                                                                                args=[Name(id='i', ctx=Load())],
                                                                                                                                keywords=[],
                                                                                                                            ),
                                                                                                                            op=Add(),
                                                                                                                            right=Constant(value=')', kind=None),
                                                                                                                        ),
                                                                                                                        attr='ljust',
                                                                                                                        ctx=Load(),
                                                                                                                    ),
                                                                                                                    args=[Name(id='cwidth', ctx=Load())],
                                                                                                                    keywords=[],
                                                                                                                ),
                                                                                                            ),
                                                                                                        ],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                ),
                                                                                                Assign(
                                                                                                    targets=[Name(id='i', ctx=Store())],
                                                                                                    value=BinOp(
                                                                                                        left=Name(id='i', ctx=Load()),
                                                                                                        op=Add(),
                                                                                                        right=Constant(value=1, kind=None),
                                                                                                    ),
                                                                                                    type_comment=None,
                                                                                                ),
                                                                                            ],
                                                                                            orelse=[],
                                                                                        ),
                                                                                        Expr(
                                                                                            value=Call(
                                                                                                func=Name(id='print_elem', ctx=Load()),
                                                                                                args=[
                                                                                                    Name(id='stylestack', ctx=Load()),
                                                                                                    Name(id='serializer', ctx=Load()),
                                                                                                    Name(id='child', ctx=Load()),
                                                                                                ],
                                                                                                keywords=[
                                                                                                    keyword(
                                                                                                        arg='indent',
                                                                                                        value=BinOp(
                                                                                                            left=Name(id='indent', ctx=Load()),
                                                                                                            op=Add(),
                                                                                                            right=Constant(value=1, kind=None),
                                                                                                        ),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[],
                                                                                    type_comment=None,
                                                                                ),
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='serializer', ctx=Load()),
                                                                                            attr='end_entity',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                If(
                                                                                    test=Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='elem', ctx=Load()),
                                                                                            attr='tag',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[Constant(value='pre', kind=None)],
                                                                                    ),
                                                                                    body=[
                                                                                        Expr(
                                                                                            value=Call(
                                                                                                func=Attribute(
                                                                                                    value=Name(id='serializer', ctx=Load()),
                                                                                                    attr='start_block',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[Name(id='stylestack', ctx=Load())],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ),
                                                                                        Expr(
                                                                                            value=Call(
                                                                                                func=Attribute(
                                                                                                    value=Name(id='serializer', ctx=Load()),
                                                                                                    attr='pre',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[
                                                                                                    Attribute(
                                                                                                        value=Name(id='elem', ctx=Load()),
                                                                                                        attr='text',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ),
                                                                                        Expr(
                                                                                            value=Call(
                                                                                                func=Attribute(
                                                                                                    value=Name(id='serializer', ctx=Load()),
                                                                                                    attr='end_entity',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[
                                                                                        If(
                                                                                            test=Compare(
                                                                                                left=Attribute(
                                                                                                    value=Name(id='elem', ctx=Load()),
                                                                                                    attr='tag',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[Constant(value='hr', kind=None)],
                                                                                            ),
                                                                                            body=[
                                                                                                Assign(
                                                                                                    targets=[Name(id='width', ctx=Store())],
                                                                                                    value=Call(
                                                                                                        func=Attribute(
                                                                                                            value=Name(id='stylestack', ctx=Load()),
                                                                                                            attr='get',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        args=[Constant(value='width', kind=None)],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                    type_comment=None,
                                                                                                ),
                                                                                                If(
                                                                                                    test=Compare(
                                                                                                        left=Call(
                                                                                                            func=Attribute(
                                                                                                                value=Name(id='stylestack', ctx=Load()),
                                                                                                                attr='get',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            args=[Constant(value='size', kind=None)],
                                                                                                            keywords=[],
                                                                                                        ),
                                                                                                        ops=[In()],
                                                                                                        comparators=[
                                                                                                            Tuple(
                                                                                                                elts=[
                                                                                                                    Constant(value='double', kind=None),
                                                                                                                    Constant(value='double-width', kind=None),
                                                                                                                ],
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                    body=[
                                                                                                        Assign(
                                                                                                            targets=[Name(id='width', ctx=Store())],
                                                                                                            value=BinOp(
                                                                                                                left=Name(id='width', ctx=Load()),
                                                                                                                op=Div(),
                                                                                                                right=Constant(value=2, kind=None),
                                                                                                            ),
                                                                                                            type_comment=None,
                                                                                                        ),
                                                                                                    ],
                                                                                                    orelse=[],
                                                                                                ),
                                                                                                Expr(
                                                                                                    value=Call(
                                                                                                        func=Attribute(
                                                                                                            value=Name(id='serializer', ctx=Load()),
                                                                                                            attr='start_block',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        args=[Name(id='stylestack', ctx=Load())],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                ),
                                                                                                Expr(
                                                                                                    value=Call(
                                                                                                        func=Attribute(
                                                                                                            value=Name(id='serializer', ctx=Load()),
                                                                                                            attr='text',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        args=[
                                                                                                            BinOp(
                                                                                                                left=Constant(value='-', kind=None),
                                                                                                                op=Mult(),
                                                                                                                right=Name(id='width', ctx=Load()),
                                                                                                            ),
                                                                                                        ],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                ),
                                                                                                Expr(
                                                                                                    value=Call(
                                                                                                        func=Attribute(
                                                                                                            value=Name(id='serializer', ctx=Load()),
                                                                                                            attr='end_entity',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        args=[],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                            orelse=[
                                                                                                If(
                                                                                                    test=Compare(
                                                                                                        left=Attribute(
                                                                                                            value=Name(id='elem', ctx=Load()),
                                                                                                            attr='tag',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        ops=[Eq()],
                                                                                                        comparators=[Constant(value='br', kind=None)],
                                                                                                    ),
                                                                                                    body=[
                                                                                                        Expr(
                                                                                                            value=Call(
                                                                                                                func=Attribute(
                                                                                                                    value=Name(id='serializer', ctx=Load()),
                                                                                                                    attr='linebreak',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                args=[],
                                                                                                                keywords=[],
                                                                                                            ),
                                                                                                        ),
                                                                                                    ],
                                                                                                    orelse=[
                                                                                                        If(
                                                                                                            test=Compare(
                                                                                                                left=Attribute(
                                                                                                                    value=Name(id='elem', ctx=Load()),
                                                                                                                    attr='tag',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                ops=[Eq()],
                                                                                                                comparators=[Constant(value='img', kind=None)],
                                                                                                            ),
                                                                                                            body=[
                                                                                                                If(
                                                                                                                    test=BoolOp(
                                                                                                                        op=And(),
                                                                                                                        values=[
                                                                                                                            Compare(
                                                                                                                                left=Constant(value='src', kind=None),
                                                                                                                                ops=[In()],
                                                                                                                                comparators=[
                                                                                                                                    Attribute(
                                                                                                                                        value=Name(id='elem', ctx=Load()),
                                                                                                                                        attr='attrib',
                                                                                                                                        ctx=Load(),
                                                                                                                                    ),
                                                                                                                                ],
                                                                                                                            ),
                                                                                                                            Compare(
                                                                                                                                left=Constant(value='data:', kind=None),
                                                                                                                                ops=[In()],
                                                                                                                                comparators=[
                                                                                                                                    Subscript(
                                                                                                                                        value=Attribute(
                                                                                                                                            value=Name(id='elem', ctx=Load()),
                                                                                                                                            attr='attrib',
                                                                                                                                            ctx=Load(),
                                                                                                                                        ),
                                                                                                                                        slice=Constant(value='src', kind=None),
                                                                                                                                        ctx=Load(),
                                                                                                                                    ),
                                                                                                                                ],
                                                                                                                            ),
                                                                                                                        ],
                                                                                                                    ),
                                                                                                                    body=[
                                                                                                                        Expr(
                                                                                                                            value=Call(
                                                                                                                                func=Attribute(
                                                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                                                    attr='print_base64_image',
                                                                                                                                    ctx=Load(),
                                                                                                                                ),
                                                                                                                                args=[
                                                                                                                                    Call(
                                                                                                                                        func=Name(id='bytes', ctx=Load()),
                                                                                                                                        args=[
                                                                                                                                            Subscript(
                                                                                                                                                value=Attribute(
                                                                                                                                                    value=Name(id='elem', ctx=Load()),
                                                                                                                                                    attr='attrib',
                                                                                                                                                    ctx=Load(),
                                                                                                                                                ),
                                                                                                                                                slice=Constant(value='src', kind=None),
                                                                                                                                                ctx=Load(),
                                                                                                                                            ),
                                                                                                                                            Constant(value='utf-8', kind=None),
                                                                                                                                        ],
                                                                                                                                        keywords=[],
                                                                                                                                    ),
                                                                                                                                ],
                                                                                                                                keywords=[],
                                                                                                                            ),
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                    orelse=[],
                                                                                                                ),
                                                                                                            ],
                                                                                                            orelse=[
                                                                                                                If(
                                                                                                                    test=BoolOp(
                                                                                                                        op=And(),
                                                                                                                        values=[
                                                                                                                            Compare(
                                                                                                                                left=Attribute(
                                                                                                                                    value=Name(id='elem', ctx=Load()),
                                                                                                                                    attr='tag',
                                                                                                                                    ctx=Load(),
                                                                                                                                ),
                                                                                                                                ops=[Eq()],
                                                                                                                                comparators=[Constant(value='barcode', kind=None)],
                                                                                                                            ),
                                                                                                                            Compare(
                                                                                                                                left=Constant(value='encoding', kind=None),
                                                                                                                                ops=[In()],
                                                                                                                                comparators=[
                                                                                                                                    Attribute(
                                                                                                                                        value=Name(id='elem', ctx=Load()),
                                                                                                                                        attr='attrib',
                                                                                                                                        ctx=Load(),
                                                                                                                                    ),
                                                                                                                                ],
                                                                                                                            ),
                                                                                                                        ],
                                                                                                                    ),
                                                                                                                    body=[
                                                                                                                        Expr(
                                                                                                                            value=Call(
                                                                                                                                func=Attribute(
                                                                                                                                    value=Name(id='serializer', ctx=Load()),
                                                                                                                                    attr='start_block',
                                                                                                                                    ctx=Load(),
                                                                                                                                ),
                                                                                                                                args=[Name(id='stylestack', ctx=Load())],
                                                                                                                                keywords=[],
                                                                                                                            ),
                                                                                                                        ),
                                                                                                                        Expr(
                                                                                                                            value=Call(
                                                                                                                                func=Attribute(
                                                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                                                    attr='barcode',
                                                                                                                                    ctx=Load(),
                                                                                                                                ),
                                                                                                                                args=[
                                                                                                                                    Call(
                                                                                                                                        func=Name(id='strclean', ctx=Load()),
                                                                                                                                        args=[
                                                                                                                                            Attribute(
                                                                                                                                                value=Name(id='elem', ctx=Load()),
                                                                                                                                                attr='text',
                                                                                                                                                ctx=Load(),
                                                                                                                                            ),
                                                                                                                                        ],
                                                                                                                                        keywords=[],
                                                                                                                                    ),
                                                                                                                                    Subscript(
                                                                                                                                        value=Attribute(
                                                                                                                                            value=Name(id='elem', ctx=Load()),
                                                                                                                                            attr='attrib',
                                                                                                                                            ctx=Load(),
                                                                                                                                        ),
                                                                                                                                        slice=Constant(value='encoding', kind=None),
                                                                                                                                        ctx=Load(),
                                                                                                                                    ),
                                                                                                                                ],
                                                                                                                                keywords=[],
                                                                                                                            ),
                                                                                                                        ),
                                                                                                                        Expr(
                                                                                                                            value=Call(
                                                                                                                                func=Attribute(
                                                                                                                                    value=Name(id='serializer', ctx=Load()),
                                                                                                                                    attr='end_entity',
                                                                                                                                    ctx=Load(),
                                                                                                                                ),
                                                                                                                                args=[],
                                                                                                                                keywords=[],
                                                                                                                            ),
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                    orelse=[
                                                                                                                        If(
                                                                                                                            test=Compare(
                                                                                                                                left=Attribute(
                                                                                                                                    value=Name(id='elem', ctx=Load()),
                                                                                                                                    attr='tag',
                                                                                                                                    ctx=Load(),
                                                                                                                                ),
                                                                                                                                ops=[Eq()],
                                                                                                                                comparators=[Constant(value='cut', kind=None)],
                                                                                                                            ),
                                                                                                                            body=[
                                                                                                                                Expr(
                                                                                                                                    value=Call(
                                                                                                                                        func=Attribute(
                                                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                                                            attr='cut',
                                                                                                                                            ctx=Load(),
                                                                                                                                        ),
                                                                                                                                        args=[],
                                                                                                                                        keywords=[],
                                                                                                                                    ),
                                                                                                                                ),
                                                                                                                            ],
                                                                                                                            orelse=[
                                                                                                                                If(
                                                                                                                                    test=Compare(
                                                                                                                                        left=Attribute(
                                                                                                                                            value=Name(id='elem', ctx=Load()),
                                                                                                                                            attr='tag',
                                                                                                                                            ctx=Load(),
                                                                                                                                        ),
                                                                                                                                        ops=[Eq()],
                                                                                                                                        comparators=[Constant(value='partialcut', kind=None)],
                                                                                                                                    ),
                                                                                                                                    body=[
                                                                                                                                        Expr(
                                                                                                                                            value=Call(
                                                                                                                                                func=Attribute(
                                                                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                                                                    attr='cut',
                                                                                                                                                    ctx=Load(),
                                                                                                                                                ),
                                                                                                                                                args=[],
                                                                                                                                                keywords=[
                                                                                                                                                    keyword(
                                                                                                                                                        arg='mode',
                                                                                                                                                        value=Constant(value='part', kind=None),
                                                                                                                                                    ),
                                                                                                                                                ],
                                                                                                                                            ),
                                                                                                                                        ),
                                                                                                                                    ],
                                                                                                                                    orelse=[
                                                                                                                                        If(
                                                                                                                                            test=Compare(
                                                                                                                                                left=Attribute(
                                                                                                                                                    value=Name(id='elem', ctx=Load()),
                                                                                                                                                    attr='tag',
                                                                                                                                                    ctx=Load(),
                                                                                                                                                ),
                                                                                                                                                ops=[Eq()],
                                                                                                                                                comparators=[Constant(value='cashdraw', kind=None)],
                                                                                                                                            ),
                                                                                                                                            body=[
                                                                                                                                                Expr(
                                                                                                                                                    value=Call(
                                                                                                                                                        func=Attribute(
                                                                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                                                                            attr='cashdraw',
                                                                                                                                                            ctx=Load(),
                                                                                                                                                        ),
                                                                                                                                                        args=[Constant(value=2, kind=None)],
                                                                                                                                                        keywords=[],
                                                                                                                                                    ),
                                                                                                                                                ),
                                                                                                                                                Expr(
                                                                                                                                                    value=Call(
                                                                                                                                                        func=Attribute(
                                                                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                                                                            attr='cashdraw',
                                                                                                                                                            ctx=Load(),
                                                                                                                                                        ),
                                                                                                                                                        args=[Constant(value=5, kind=None)],
                                                                                                                                                        keywords=[],
                                                                                                                                                    ),
                                                                                                                                                ),
                                                                                                                                            ],
                                                                                                                                            orelse=[],
                                                                                                                                        ),
                                                                                                                                    ],
                                                                                                                                ),
                                                                                                                            ],
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                ),
                                                                                                            ],
                                                                                                        ),
                                                                                                    ],
                                                                                                ),
                                                                                            ],
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='stylestack', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='stylestack', ctx=Store())],
                                    value=Call(
                                        func=Name(id='StyleStack', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='serializer', ctx=Store())],
                                    value=Call(
                                        func=Name(id='XmlSerializer', ctx=Load()),
                                        args=[Name(id='self', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='root', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='ET', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='xml', ctx=Load()),
                                                    attr='encode',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='utf-8', kind=None)],
                                                keywords=[],
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
                                            attr='_raw',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='stylestack', ctx=Load()),
                                                    attr='to_escpos',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='print_elem', ctx=Load()),
                                        args=[
                                            Name(id='stylestack', ctx=Load()),
                                            Name(id='serializer', ctx=Load()),
                                            Name(id='root', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Constant(value='open-cashdrawer', kind=None),
                                                ops=[In()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='root', ctx=Load()),
                                                        attr='attrib',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='root', ctx=Load()),
                                                        attr='attrib',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='open-cashdrawer', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='true', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cashdraw',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=2, kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cashdraw',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=5, kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Compare(
                                                    left=Constant(value='cut', kind=None),
                                                    ops=[In()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='root', ctx=Load()),
                                                            attr='attrib',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            Compare(
                                                left=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='root', ctx=Load()),
                                                        attr='attrib',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='cut', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='true', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cut',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='e',
                                    body=[
                                        Assign(
                                            targets=[Name(id='errmsg', ctx=Store())],
                                            value=BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=BinOp(
                                                            left=BinOp(
                                                                left=BinOp(
                                                                    left=Call(
                                                                        func=Name(id='str', ctx=Load()),
                                                                        args=[Name(id='e', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    op=Add(),
                                                                    right=Constant(value='\n', kind=None),
                                                                ),
                                                                op=Add(),
                                                                right=BinOp(
                                                                    left=Constant(value='-', kind=None),
                                                                    op=Mult(),
                                                                    right=Constant(value=48, kind=None),
                                                                ),
                                                            ),
                                                            op=Add(),
                                                            right=Constant(value='\n', kind=None),
                                                        ),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Attribute(
                                                                value=Name(id='traceback', ctx=Load()),
                                                                attr='format_exc',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    op=Add(),
                                                    right=BinOp(
                                                        left=Constant(value='-', kind=None),
                                                        op=Mult(),
                                                        right=Constant(value=48, kind=None),
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Constant(value='\n', kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='text',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='errmsg', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cut',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Raise(
                                            exc=Name(id='e', ctx=Load()),
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
                FunctionDef(
                    name='text',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='txt', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Print Utf8 encoded alpha-numeric text ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='txt', ctx=Load()),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='txt', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='txt', ctx=Load()),
                                            attr='decode',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='utf-8', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=None,
                                    name=None,
                                    body=[
                                        Try(
                                            body=[
                                                Assign(
                                                    targets=[Name(id='txt', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='txt', ctx=Load()),
                                                            attr='decode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='utf-16', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=None,
                                                    name=None,
                                                    body=[Pass()],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='extra_chars',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='encode_char',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='char', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value=' \n            Encodes a single utf-8 character into a sequence of \n            esc-pos code page change instructions and character declarations \n            ', kind=None),
                                ),
                                Assign(
                                    targets=[Name(id='char_utf8', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='char', ctx=Load()),
                                            attr='encode',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='utf-8', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='encoded', ctx=Store())],
                                    value=Constant(value='', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='encoding', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='encoding',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='encodings', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='cp437', kind=None),
                                            Constant(value='cp850', kind=None),
                                            Constant(value='cp852', kind=None),
                                            Constant(value='cp857', kind=None),
                                            Constant(value='cp858', kind=None),
                                            Constant(value='cp860', kind=None),
                                            Constant(value='cp863', kind=None),
                                            Constant(value='cp865', kind=None),
                                            Constant(value='cp1251', kind=None),
                                            Constant(value='cp866', kind=None),
                                            Constant(value='cp862', kind=None),
                                            Constant(value='cp720', kind=None),
                                            Constant(value='cp936', kind=None),
                                            Constant(value='iso8859_2', kind=None),
                                            Constant(value='iso8859_7', kind=None),
                                            Constant(value='iso8859_9', kind=None),
                                            Constant(value='cp1254', kind=None),
                                            Constant(value='cp1255', kind=None),
                                            Constant(value='cp1256', kind=None),
                                            Constant(value='cp1257', kind=None),
                                            Constant(value='cp1258', kind=None),
                                            Constant(value='katakana', kind=None),
                                        ],
                                        values=[
                                            Name(id='TXT_ENC_PC437', ctx=Load()),
                                            Name(id='TXT_ENC_PC850', ctx=Load()),
                                            Name(id='TXT_ENC_PC852', ctx=Load()),
                                            Name(id='TXT_ENC_PC857', ctx=Load()),
                                            Name(id='TXT_ENC_PC858', ctx=Load()),
                                            Name(id='TXT_ENC_PC860', ctx=Load()),
                                            Name(id='TXT_ENC_PC863', ctx=Load()),
                                            Name(id='TXT_ENC_PC865', ctx=Load()),
                                            Name(id='TXT_ENC_WPC1251', ctx=Load()),
                                            Name(id='TXT_ENC_PC866', ctx=Load()),
                                            Name(id='TXT_ENC_PC862', ctx=Load()),
                                            Name(id='TXT_ENC_PC720', ctx=Load()),
                                            Name(id='TXT_ENC_PC936', ctx=Load()),
                                            Name(id='TXT_ENC_8859_2', ctx=Load()),
                                            Name(id='TXT_ENC_8859_7', ctx=Load()),
                                            Name(id='TXT_ENC_8859_9', ctx=Load()),
                                            Name(id='TXT_ENC_WPC1254', ctx=Load()),
                                            Name(id='TXT_ENC_WPC1255', ctx=Load()),
                                            Name(id='TXT_ENC_WPC1256', ctx=Load()),
                                            Name(id='TXT_ENC_WPC1257', ctx=Load()),
                                            Name(id='TXT_ENC_WPC1258', ctx=Load()),
                                            Name(id='TXT_ENC_KATAKANA', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='remaining', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='copy', ctx=Load()),
                                            attr='copy',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='encodings', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='encoding', ctx=Load()),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='encoding', ctx=Store())],
                                            value=Constant(value='cp437', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                While(
                                    test=Constant(value=True, kind=None),
                                    body=[
                                        Try(
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='encoding', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='katakana', kind=None)],
                                                    ),
                                                    body=[
                                                        If(
                                                            test=Name(id='jcconv', ctx=Load()),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='kata', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='jcconv', ctx=Load()),
                                                                            attr='kata2half',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='jcconv', ctx=Load()),
                                                                                    attr='hira2kata',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='char_utf8', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Compare(
                                                                        left=Name(id='kata', ctx=Load()),
                                                                        ops=[NotEq()],
                                                                        comparators=[Name(id='char_utf8', ctx=Load())],
                                                                    ),
                                                                    body=[
                                                                        AugAssign(
                                                                            target=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='extra_chars',
                                                                                ctx=Store(),
                                                                            ),
                                                                            op=Add(),
                                                                            value=BinOp(
                                                                                left=Call(
                                                                                    func=Name(id='len', ctx=Load()),
                                                                                    args=[
                                                                                        Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='kata', ctx=Load()),
                                                                                                attr='decode',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='utf-8', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                op=Sub(),
                                                                                right=Constant(value=1, kind=None),
                                                                            ),
                                                                        ),
                                                                        Return(
                                                                            value=Call(
                                                                                func=Name(id='encode_str', ctx=Load()),
                                                                                args=[
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='kata', ctx=Load()),
                                                                                            attr='decode',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='utf-8', kind=None)],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[Name(id='kata', ctx=Store())],
                                                                    value=Name(id='char_utf8', ctx=Load()),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='kata', ctx=Load()),
                                                                ops=[In()],
                                                                comparators=[Name(id='TXT_ENC_KATAKANA_MAP', ctx=Load())],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='encoded', ctx=Store())],
                                                                    value=Subscript(
                                                                        value=Name(id='TXT_ENC_KATAKANA_MAP', ctx=Load()),
                                                                        slice=Name(id='kata', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Break(),
                                                            ],
                                                            orelse=[
                                                                Raise(
                                                                    exc=Call(
                                                                        func=Name(id='ValueError', ctx=Load()),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    cause=None,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[Name(id='encoded', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='char', ctx=Load()),
                                                                    attr='encode',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='encoding', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Call(
                                                                    func=Name(id='ord', ctx=Load()),
                                                                    args=[Name(id='encoded', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                ops=[LtE()],
                                                                comparators=[Constant(value=127, kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='encoding', ctx=Store())],
                                                                    value=Constant(value='cp437', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        Break(),
                                                    ],
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Tuple(
                                                        elts=[
                                                            Name(id='UnicodeEncodeError', ctx=Load()),
                                                            Name(id='UnicodeWarning', ctx=Load()),
                                                            Name(id='TypeError', ctx=Load()),
                                                            Name(id='ValueError', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    name=None,
                                                    body=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='encoding', ctx=Load()),
                                                                ops=[In()],
                                                                comparators=[Name(id='remaining', ctx=Load())],
                                                            ),
                                                            body=[
                                                                Delete(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='remaining', ctx=Load()),
                                                                            slice=Name(id='encoding', ctx=Load()),
                                                                            ctx=Del(),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Call(
                                                                    func=Name(id='len', ctx=Load()),
                                                                    args=[Name(id='remaining', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                ops=[GtE()],
                                                                comparators=[Constant(value=1, kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Name(id='encoding', ctx=Store()),
                                                                                Name(id='_', ctx=Store()),
                                                                            ],
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='remaining', ctx=Load()),
                                                                            attr='popitem',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[Name(id='encoding', ctx=Store())],
                                                                    value=Constant(value='cp437', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='encoded', ctx=Store())],
                                                                    value=Constant(value=b'\xb1', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                                Break(),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='encoding', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='encoding',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='encoding',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='encoding', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='encoded', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Name(id='bytes', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Name(id='encodings', ctx=Load()),
                                                            slice=Name(id='encoding', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        Constant(value='utf-8', kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Name(id='encoded', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Name(id='encoded', ctx=Load()),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='encode_str',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='txt', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='buffer', ctx=Store())],
                                    value=Constant(value=b'', kind=None),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='c', ctx=Store()),
                                    iter=Name(id='txt', ctx=Load()),
                                    body=[
                                        AugAssign(
                                            target=Name(id='buffer', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Name(id='encode_char', ctx=Load()),
                                                args=[Name(id='c', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Return(
                                    value=Name(id='buffer', ctx=Load()),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='txt', ctx=Store())],
                            value=Call(
                                func=Name(id='encode_str', ctx=Load()),
                                args=[Name(id='txt', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        While(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='extra_chars',
                                    ctx=Load(),
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='dspace', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='txt', ctx=Load()),
                                            attr='find',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='  ', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='dspace', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='txt', ctx=Store())],
                                            value=BinOp(
                                                left=Subscript(
                                                    value=Name(id='txt', ctx=Load()),
                                                    slice=Slice(
                                                        lower=None,
                                                        upper=Name(id='dspace', ctx=Load()),
                                                        step=None,
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Subscript(
                                                    value=Name(id='txt', ctx=Load()),
                                                    slice=Slice(
                                                        lower=BinOp(
                                                            left=Name(id='dspace', ctx=Load()),
                                                            op=Add(),
                                                            right=Constant(value=1, kind=None),
                                                        ),
                                                        upper=None,
                                                        step=None,
                                                    ),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='extra_chars',
                                                ctx=Store(),
                                            ),
                                            op=Sub(),
                                            value=Constant(value=1, kind=None),
                                        ),
                                    ],
                                    orelse=[Break()],
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_raw',
                                    ctx=Load(),
                                ),
                                args=[Name(id='txt', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='set',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='align', annotation=None, type_comment=None),
                            arg(arg='font', annotation=None, type_comment=None),
                            arg(arg='type', annotation=None, type_comment=None),
                            arg(arg='width', annotation=None, type_comment=None),
                            arg(arg='height', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value='left', kind=None),
                            Constant(value='a', kind=None),
                            Constant(value='normal', kind=None),
                            Constant(value=1, kind=None),
                            Constant(value=1, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Set text properties ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='align', ctx=Load()),
                                        attr='upper',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='CENTER', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raw',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='TXT_ALIGN_CT', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='align', ctx=Load()),
                                                attr='upper',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='RIGHT', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_raw',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='TXT_ALIGN_RT', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='align', ctx=Load()),
                                                        attr='upper',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='LEFT', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_raw',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='TXT_ALIGN_LT', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='font', ctx=Load()),
                                        attr='upper',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='B', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raw',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='TXT_FONT_B', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raw',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='TXT_FONT_A', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='type', ctx=Load()),
                                        attr='upper',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='B', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raw',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='TXT_BOLD_ON', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raw',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='TXT_UNDERL_OFF', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='type', ctx=Load()),
                                                attr='upper',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='U', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_raw',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='TXT_BOLD_OFF', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_raw',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='TXT_UNDERL_ON', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='type', ctx=Load()),
                                                        attr='upper',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='U2', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_raw',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='TXT_BOLD_OFF', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_raw',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='TXT_UNDERL2_ON', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='type', ctx=Load()),
                                                                attr='upper',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='BU', kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_raw',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='TXT_BOLD_ON', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_raw',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='TXT_UNDERL_ON', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='type', ctx=Load()),
                                                                        attr='upper',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='BU2', kind=None)],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_raw',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='TXT_BOLD_ON', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_raw',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='TXT_UNDERL2_ON', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='type', ctx=Load()),
                                                                            attr='upper',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='NORMAL', kind=None)],
                                                                    ),
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='_raw',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='TXT_BOLD_OFF', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='_raw',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='TXT_UNDERL_OFF', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='width', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value=2, kind=None)],
                                    ),
                                    Compare(
                                        left=Name(id='height', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[Constant(value=2, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raw',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='TXT_NORMAL', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raw',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='TXT_2WIDTH', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='height', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value=2, kind=None)],
                                            ),
                                            Compare(
                                                left=Name(id='width', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Constant(value=2, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_raw',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='TXT_NORMAL', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_raw',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='TXT_2HEIGHT', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='height', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value=2, kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Name(id='width', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value=2, kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_raw',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='TXT_2WIDTH', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_raw',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='TXT_2HEIGHT', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_raw',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='TXT_NORMAL', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='cut',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='mode', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value='', kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Cut paper ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_raw',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='\n\n\n\n\n\n', kind=None)],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='mode', ctx=Load()),
                                        attr='upper',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='PART', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raw',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='PAPER_PART_CUT', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raw',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='PAPER_FULL_CUT', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='cashdraw',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='pin', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Send pulse to kick the cash drawer\n\n        For some reason, with some printers (ex: Epson TM-m30), the cash drawer\n        only opens 50% of the time if you just send the pulse. But if you read\n        the status afterwards, it opens all the time.\n        ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='pin', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value=2, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raw',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='CD_KICK_2', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='pin', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value=5, kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_raw',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='CD_KICK_5', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='CashDrawerError', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_printer_status',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='hw',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='hw', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Hardware operations ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='hw', ctx=Load()),
                                        attr='upper',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='INIT', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raw',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='HW_INIT', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='hw', ctx=Load()),
                                                attr='upper',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='SELECT', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_raw',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='HW_SELECT', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='hw', ctx=Load()),
                                                        attr='upper',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='RESET', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_raw',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='HW_RESET', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[Pass()],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='control',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='ctl', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Feed control sequences ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='ctl', ctx=Load()),
                                        attr='upper',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='LF', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_raw',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='CTL_LF', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='ctl', ctx=Load()),
                                                attr='upper',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='FF', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_raw',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='CTL_FF', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='ctl', ctx=Load()),
                                                        attr='upper',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='CR', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_raw',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='CTL_CR', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='ctl', ctx=Load()),
                                                                attr='upper',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='HT', kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_raw',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='CTL_HT', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='ctl', ctx=Load()),
                                                                        attr='upper',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='VT', kind=None)],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_raw',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='CTL_VT', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
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
