# aws-serverless-pipeline

Event-Driven Serverless Media Pipeline
An asynchronous, event-driven pipeline built on AWS to automatically process object storage uploads. This project eliminates idle server costs by using serverless compute that scales from zero to concurrent execution exactly when an S3 event fires, routing success alerts to a pub/sub messaging topic.

Architecture
[arch.drawio](https://github.com/user-attachments/files/32644877/arch.drawio)
<mxfile host="app.diagrams.net">
  <diagram name="Page-1" id="entef-k-Psu2nJqBH-Vz">
    <mxGraphModel dx="1414" dy="752" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="ZjXssGQfS69yWw1hF0dT-1" parent="1" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#7AA116;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.s3;" value="S3 (Raw Media Bucket)" vertex="1">
          <mxGeometry height="78" width="78" x="70" y="170" as="geometry" />
        </mxCell>
        <mxCell id="ZjXssGQfS69yWw1hF0dT-2" parent="1" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.lambda;" value="AWS Lambda (Image Processor)" vertex="1">
          <mxGeometry height="78" width="78" x="330" y="170" as="geometry" />
        </mxCell>
        <mxCell id="ZjXssGQfS69yWw1hF0dT-3" edge="1" parent="1" source="ZjXssGQfS69yWw1hF0dT-1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;" target="ZjXssGQfS69yWw1hF0dT-2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="ZjXssGQfS69yWw1hF0dT-4" connectable="0" parent="ZjXssGQfS69yWw1hF0dT-3" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" value="S3 Event Notification" vertex="1">
          <mxGeometry relative="1" x="0.0984" y="-1" as="geometry">
            <mxPoint x="-6" y="-1" as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZjXssGQfS69yWw1hF0dT-5" parent="1" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#7AA116;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.s3;" value="S3 (Processed Media Bucket)" vertex="1">
          <mxGeometry height="78" width="78" x="630" y="70" as="geometry" />
        </mxCell>
        <mxCell id="ZjXssGQfS69yWw1hF0dT-12" edge="1" parent="1" source="ZjXssGQfS69yWw1hF0dT-6" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" target="ZjXssGQfS69yWw1hF0dT-11">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="ZjXssGQfS69yWw1hF0dT-13" connectable="0" parent="ZjXssGQfS69yWw1hF0dT-12" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" value="Email Delivery" vertex="1">
          <mxGeometry relative="1" x="-0.0714" y="-1" as="geometry">
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZjXssGQfS69yWw1hF0dT-6" parent="1" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#E7157B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sns;" value="Amazon SNS (Topic)" vertex="1">
          <mxGeometry height="78" width="78" x="630" y="270" as="geometry" />
        </mxCell>
        <mxCell id="ZjXssGQfS69yWw1hF0dT-7" edge="1" parent="1" source="ZjXssGQfS69yWw1hF0dT-2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;" target="ZjXssGQfS69yWw1hF0dT-6">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="480" y="209" />
              <mxPoint x="480" y="309" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="ZjXssGQfS69yWw1hF0dT-10" connectable="0" parent="ZjXssGQfS69yWw1hF0dT-7" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" value="Publish success alert" vertex="1">
          <mxGeometry relative="1" x="0.6159" as="geometry">
            <mxPoint x="-12" as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZjXssGQfS69yWw1hF0dT-8" edge="1" parent="1" source="ZjXssGQfS69yWw1hF0dT-2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;" target="ZjXssGQfS69yWw1hF0dT-5">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="480" y="209" />
              <mxPoint x="480" y="109" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="ZjXssGQfS69yWw1hF0dT-9" connectable="0" parent="ZjXssGQfS69yWw1hF0dT-8" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" value="Save processed file" vertex="1">
          <mxGeometry relative="1" x="0.6777" y="-1" as="geometry">
            <mxPoint x="-21" y="-1" as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="ZjXssGQfS69yWw1hF0dT-11" parent="1" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.email_2;" value="" vertex="1">
          <mxGeometry height="49" width="78" x="830" y="284.5" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>


Amazon S3 (Input): Receives raw media uploads.

S3 Event Notifications: Triggers an execution event on object creation.

AWS Lambda: Extracts metadata, dynamically maps the destination bucket, and writes the output file.

Amazon S3 (Output): Stores the processed artifact.

Amazon SNS: Fans out a real-time completion alert to subscribed email endpoints.

Core Architectural Decisions
Preventing Recursive Loops: Specifically separated the trigger source (raw-media bucket) from the destination (processed-media bucket). Writing back to the trigger bucket is an anti-pattern that causes infinite Lambda invocation loops.

Least-Privilege IAM: Execution role restricted to s3:GetObject on the raw bucket, s3:PutObject on the processed bucket, and sns:Publish on the exact topic ARN.

Stateless Routing: Boto3 dynamically maps the destination bucket based on the incoming event payload (src_bucket.replace("raw", "processed")) rather than hardcoding endpoints, making the code environment-agnostic.

Observability & Verification
The pipeline was tested in us-east-1 and verified via CloudWatch logs.

S3 Trigger & Event Routing
Below: The S3 source trigger successfully invoking the processor, and the decoupled processed file landing in the destination bucket.

CloudWatch Telemetry
Below: End-to-end execution completed in ~522 ms utilizing 100 MB of the allocated 128 MB memory footprint.

SNS Alert Delivery
Below: The resulting fan-out email notification confirming the precise file processed.
