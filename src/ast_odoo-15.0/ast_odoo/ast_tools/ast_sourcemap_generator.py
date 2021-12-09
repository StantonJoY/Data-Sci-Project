Module(
    body=[
        ImportFrom(
            module='functools',
            names=[alias(name='lru_cache', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        ClassDef(
            name='SourceMapGenerator',
            bases=[],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n    The SourceMapGenerator creates the sourcemap maps the asset bundle to the js/css files.\n\n    What is a sourcemap ? (https://developer.mozilla.org/en-US/docs/Tools/Debugger/How_to/Use_a_source_map)\n    In brief: a source map is what makes possible to debug your processed/compiled/minified code as if you were\n    debugging the original, non-altered source code. It is a file that provides a mapping original <=> processed for\n    the browser to read.\n\n    This implementation of the SourceMapGenerator is a translation and adaptation of this implementation\n    in js https://github.com/mozilla/source-map. For performance purposes, we have removed all unnecessary\n    functions/steps for our use case. This simpler version does a line by line mapping, with the ability to\n    add offsets at the start and end of a file. (when we have to add comments on top a transpiled file by example).\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='source_root', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_file',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_source_root',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='source_root', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_sources',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_mappings',
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
                                    attr='_sources_contents',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_version',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=3, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_cache',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_serialize_mappings',
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
                            value=Constant(value='\n        A source map mapping is encoded with the base 64 VLQ format.\n        This function encodes the readable source to the format.\n\n        :return the encoded content\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='previous_generated_line', ctx=Store())],
                            value=Constant(value=1, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='previous_original_line', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='previous_source', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='encoded_column', ctx=Store())],
                            value=Call(
                                func=Name(id='base64vlq_encode', ctx=Load()),
                                args=[Constant(value=0, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='mapping', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_mappings',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='mapping', ctx=Load()),
                                            slice=Constant(value='generatedLine', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Name(id='previous_generated_line', ctx=Load())],
                                    ),
                                    body=[
                                        While(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='mapping', ctx=Load()),
                                                    slice=Constant(value='generatedLine', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Gt()],
                                                comparators=[Name(id='previous_generated_line', ctx=Load())],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='result', ctx=Store()),
                                                    op=Add(),
                                                    value=Constant(value=';', kind=None),
                                                ),
                                                AugAssign(
                                                    target=Name(id='previous_generated_line', ctx=Store()),
                                                    op=Add(),
                                                    value=Constant(value=1, kind=None),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='mapping', ctx=Load()),
                                            slice=Constant(value='source', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='sourceIdx', ctx=Store())],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_sources',
                                                    ctx=Load(),
                                                ),
                                                slice=Subscript(
                                                    value=Name(id='mapping', ctx=Load()),
                                                    slice=Constant(value='source', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='source', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='sourceIdx', ctx=Load()),
                                                op=Sub(),
                                                right=Name(id='previous_source', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='previous_source', ctx=Store())],
                                            value=Name(id='sourceIdx', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='line', ctx=Store())],
                                            value=BinOp(
                                                left=BinOp(
                                                    left=Subscript(
                                                        value=Name(id='mapping', ctx=Load()),
                                                        slice=Constant(value='originalLine', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                                op=Sub(),
                                                right=Name(id='previous_original_line', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='previous_original_line', ctx=Store())],
                                            value=BinOp(
                                                left=Subscript(
                                                    value=Name(id='mapping', ctx=Load()),
                                                    slice=Constant(value='originalLine', kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Tuple(
                                            elts=[
                                                Name(id='source', ctx=Load()),
                                                Name(id='line', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_cache',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_cache',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Tuple(
                                                        elts=[
                                                            Name(id='source', ctx=Load()),
                                                            Name(id='line', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Constant(value='', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Name(id='encoded_column', ctx=Load()),
                                                            Call(
                                                                func=Name(id='base64vlq_encode', ctx=Load()),
                                                                args=[Name(id='source', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Name(id='base64vlq_encode', ctx=Load()),
                                                                args=[Name(id='line', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Name(id='encoded_column', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                AugAssign(
                                    target=Name(id='result', ctx=Store()),
                                    op=Add(),
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_cache',
                                            ctx=Load(),
                                        ),
                                        slice=Tuple(
                                            elts=[
                                                Name(id='source', ctx=Load()),
                                                Name(id='line', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='to_json',
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
                            value=Constant(value='\n        Generates the json sourcemap.\n        It is the main function that assembles all the pieces.\n\n        :return {str} valid sourcemap in json format\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='mapping', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='version', kind=None),
                                    Constant(value='sources', kind=None),
                                    Constant(value='mappings', kind=None),
                                    Constant(value='sourcesContent', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_version',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_sources',
                                                        ctx=Load(),
                                                    ),
                                                    attr='keys',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_serialize_mappings',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    ListComp(
                                        elt=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_sources_contents',
                                                ctx=Load(),
                                            ),
                                            slice=Name(id='source', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='source', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_sources',
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_file',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='mapping', ctx=Load()),
                                            slice=Constant(value='file', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_file',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_source_root',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='mapping', ctx=Load()),
                                            slice=Constant(value='sourceRoot', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_source_root',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='mapping', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_content',
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
                            value=Constant(value='Generates the content of the sourcemap.\n\n        :return the content of the sourcemap as a string encoded in UTF-8.\n        ', kind=None),
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value=b")]}'\n", kind=None),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='dumps',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='to_json',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='encode',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='utf8', kind=None)],
                                    keywords=[],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='add_source',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='source_name', annotation=None, type_comment=None),
                            arg(arg='source_content', annotation=None, type_comment=None),
                            arg(arg='last_index', annotation=None, type_comment=None),
                            arg(arg='start_offset', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=0, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Adds a new source file in the sourcemap. All the lines of the source file will be mapped line by line\n        to the generated file from the (last_index + start_offset). All lines between\n        last_index and (last_index + start_offset) will\n        be mapped to line 1 of the source file.\n\n        Example:\n            ls 1 = Line 1 from new source file\n            lg 1 = Line 1 from genereted file\n            ls 1 <=> lg 1 Line 1 from new source file is map to  Line 1 from genereted file\n            nb_ls = number of lines in the new source file\n\n            Step 1:\n            ls 1 <=> lg last_index + 1\n\n            Step 2:\n            ls 1 <=> lg last_index + start_offset + 1\n            ls 2 <=> lg last_index + start_offset + 2\n            ...\n            ls nb_ls <=> lg last_index + start_offset + nb_ls\n\n\n        :param source_name: name of the source to add\n        :param source_content: content of the source to add\n        :param last_index: Line where we start to map the new source\n        :param start_offset: Number of lines to pass in the generated file before starting mapping line by line\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='source_line_count', ctx=Store())],
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='source_content', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='\n', kind=None)],
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_sources',
                                        ctx=Load(),
                                    ),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='source_name', ctx=Load()),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_sources',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_sources_contents',
                                        ctx=Load(),
                                    ),
                                    slice=Name(id='source_name', ctx=Load()),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='source_content', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='start_offset', ctx=Load()),
                                ops=[Gt()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_mappings',
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='generatedLine', kind=None),
                                                    Constant(value='originalLine', kind=None),
                                                    Constant(value='source', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=Name(id='last_index', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                    Constant(value=1, kind=None),
                                                    Name(id='source_name', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    Constant(value=1, kind=None),
                                    BinOp(
                                        left=Name(id='source_line_count', ctx=Load()),
                                        op=Add(),
                                        right=Constant(value=1, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_mappings',
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='generatedLine', kind=None),
                                                    Constant(value='originalLine', kind=None),
                                                    Constant(value='source', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Name(id='last_index', ctx=Load()),
                                                            op=Add(),
                                                            right=Name(id='i', ctx=Load()),
                                                        ),
                                                        op=Add(),
                                                        right=Name(id='start_offset', ctx=Load()),
                                                    ),
                                                    Name(id='i', ctx=Load()),
                                                    Name(id='source_name', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
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
            ],
            decorator_list=[],
        ),
        Assign(
            targets=[Name(id='B64CHARS', ctx=Store())],
            value=Constant(value=b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[
                Tuple(
                    elts=[
                        Name(id='SHIFTSIZE', ctx=Store()),
                        Name(id='FLAG', ctx=Store()),
                        Name(id='MASK', ctx=Store()),
                    ],
                    ctx=Store(),
                ),
            ],
            value=Tuple(
                elts=[
                    Constant(value=5, kind=None),
                    BinOp(
                        left=Constant(value=1, kind=None),
                        op=LShift(),
                        right=Constant(value=5, kind=None),
                    ),
                    BinOp(
                        left=BinOp(
                            left=Constant(value=1, kind=None),
                            op=LShift(),
                            right=Constant(value=5, kind=None),
                        ),
                        op=Sub(),
                        right=Constant(value=1, kind=None),
                    ),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='base64vlq_encode',
            args=arguments(
                posonlyargs=[],
                args=[],
                vararg=arg(arg='values', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Encode Base64 VLQ encoded sequences\n    https://gist.github.com/mjpieters/86b0d152bb51d5f5979346d11005588b\n    Base64 VLQ is used in source maps.\n    VLQ values consist of 6 bits (matching the 64 characters of the Base64\n    alphabet), with the most significant bit a *continuation* flag. If the\n    flag is set, then the next character in the input is part of the same\n    integer value. Multiple VLQ character sequences so form an unbounded\n    integer value, in little-endian order.\n    The *first* VLQ value consists of a continuation flag, 4 bits for the\n    value, and the last bit the *sign* of the integer:\n    +-----+-----+-----+-----+-----+-----+\n    |  c  |  b3 |  b2 |  b1 |  b0 |  s  |\n    +-----+-----+-----+-----+-----+-----+\n    while subsequent VLQ characters contain 5 bits of value:\n    +-----+-----+-----+-----+-----+-----+\n    |  c  |  b4 |  b3 |  b2 |  b1 |  b0 |\n    +-----+-----+-----+-----+-----+-----+\n    For source maps, Base64 VLQ sequences can contain 1, 4 or 5 elements.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='results', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='add', ctx=Store())],
                    value=Attribute(
                        value=Name(id='results', ctx=Load()),
                        attr='append',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='v', ctx=Store()),
                    iter=Name(id='values', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='v', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Call(
                                        func=Name(id='abs', ctx=Load()),
                                        args=[Name(id='v', ctx=Load())],
                                        keywords=[],
                                    ),
                                    op=LShift(),
                                    right=Constant(value=1, kind=None),
                                ),
                                op=BitOr(),
                                right=Call(
                                    func=Name(id='int', ctx=Load()),
                                    args=[
                                        Compare(
                                            left=Name(id='v', ctx=Load()),
                                            ops=[Lt()],
                                            comparators=[Constant(value=0, kind=None)],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        While(
                            test=Constant(value=True, kind=None),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='toencode', ctx=Store()),
                                                Name(id='v', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Tuple(
                                        elts=[
                                            BinOp(
                                                left=Name(id='v', ctx=Load()),
                                                op=BitAnd(),
                                                right=Name(id='MASK', ctx=Load()),
                                            ),
                                            BinOp(
                                                left=Name(id='v', ctx=Load()),
                                                op=RShift(),
                                                right=Name(id='SHIFTSIZE', ctx=Load()),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='add', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Name(id='toencode', ctx=Load()),
                                                op=BitOr(),
                                                right=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Name(id='v', ctx=Load()),
                                                        Name(id='FLAG', ctx=Load()),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='v', ctx=Load()),
                                    ),
                                    body=[Break()],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Name(id='bytes', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='map', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='B64CHARS', ctx=Load()),
                                                attr='__getitem__',
                                                ctx=Load(),
                                            ),
                                            Name(id='results', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            attr='decode',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='lru_cache', ctx=Load()),
                    args=[],
                    keywords=[
                        keyword(
                            arg='maxsize',
                            value=Constant(value=64, kind=None),
                        ),
                    ],
                ),
            ],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
